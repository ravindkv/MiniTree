import FWCore.ParameterSet.Config as cms
from TopQuarkAnalysis.TopObjectResolutions.stringResolutions_etEtaPhi_Fall11_cff import *
from MiniTree.Utilities.JetEnergyScale_cfi import *

process = cms.Process("TEST")
## add message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('TtSemiLepKinFitter')
process.MessageLogger.categories.append('KinFitter')
process.MessageLogger.cerr.TtSemiLepKinFitter = cms.untracked.PSet(
    limit = cms.untracked.int32(-1)
)
process.MessageLogger.cerr.KinFitter = cms.untracked.PSet(
    limit = cms.untracked.int32(-1)
)
#def addSemiLepKinFitMuon(process, isData=False) :
isData=False
## std sequence to produce the kinematic fit for semi-leptonic events
process.load("TopQuarkAnalysis.TopKinFitter.TtSemiLepKinFitProducer_Muons_cfi")
process.load( "PhysicsTools.PatAlgos.patSequences_cff" )

## define input
process.source = cms.Source("PoolSource",
        #fileNames = cms.untracked.vstring('file:FEDED4C8-573B-E611-9ED6-0025904CF102.root')
    fileNames = cms.untracked.vstring('/store/mc/RunIISpring16MiniAODv1/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FED53EE4-7D16-E611-AE17-B083FED406AD.root')
)

## define maximal number of events to loop over
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50)
)

## configure process options
process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
    wantSummary      = cms.untracked.bool(True)
)
## configure geometry & conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.load("Configuration.StandardSequences.MagneticField_cff")

process.kinFitTtSemiLepEvent.constraints = [1,2]
'''
process.kinFitTtSemiLepEvent.jets=cms.InputTag('slimmedJets')
process.kinFitTtSemiLepEvent.leps=cms.InputTag('slimmedMuons')
process.kinFitTtSemiLepEvent.mets=cms.InputTag('slimmedMETs')
'''

#smear the JetEnergy for JER in case of MC, don't use this scaled collection for Data
process.scaledJetEnergyNominal = scaledJetEnergy.clone()
process.scaledJetEnergyNominal.inputJets = "slimmedJets"
process.scaledJetEnergyNominal.inputMETs = "slimmedMETs"
process.scaledJetEnergyNominal.scaleType = "jer"
process.scaledJetEnergyNominal.resolutionEtaRanges = cms.vdouble(
0.0, 0.5, 0.5, 1.1, 1.1, 1.7, 1.7, 2.3, 2.3, -1.0 )
process.scaledJetEnergyNominal.resolutionFactors = cms.vdouble(
1.052, 1.057, 1.096, 1.134, 1.288 )

#apply selections on muon
process.cleanPatMuons.preselection = cms.string("pt>25 && abs(eta)<2.1"+
" && isGlobalMuon && isPFMuon && isTrackerMuon" +
" && globalTrack.isNonnull "+
" && globalTrack.normalizedChi2<10"+
" && globalTrack.hitPattern.numberOfValidMuonHits>0"+
" && numberOfMatchedStations>1"+
" && innerTrack.hitPattern.numberOfValidPixelHits>0"+
" && track.hitPattern.trackerLayersWithMeasurement > 5"+
" && dB() < 0.2"+
" && (pfIsolationR04.sumChargedHadronPt+ max(0.,pfIsolationR04.sumNeutralHadronEt+pfIsolationR04.sumPhotonEt-0.5*pfIsolationR04.sumPUPt))/pt < 0.30"
)
#clean jets from muons
process.cleanPatJets.checkOverlaps.muons.requireNoOverlaps  = cms.bool(True)
process.cleanPatJets.preselection = cms.string("pt>20 && abs(eta)<2.5")

#only used for data

process.cleanPatJetsResCor = process.cleanPatJets.clone()
process.cleanPatJetsResCor.src = cms.InputTag("selectedPatJetsResCor")
process.cleanPatJetsResCor.preselection = cms.string("pt>24 && abs(eta)<2.5")


#change constraints on kineFit
# The following variables are defined in :
# TopQuarkAnalysis/TopKinFitter/python/TtSemiLepKinFitProducer_Muons_cfi.py
process.kinFitTtSemiLepEvent.mTop = cms.double(172.5)
process.kinFitTtSemiLepEvent.constraints = cms.vuint32(3, 4)
process.kinFitTtSemiLepEvent.maxNJets = cms.int32(-1)
process.kinFitTtSemiLepEvent.jets = cms.InputTag("slimmedJets")

if isData:
    process.kinFitTtSemiLepEvent.jets = cms.InputTag("cleanPatJetsResCor")

process.kinFitTtSemiLepEvent.leps = cms.InputTag("slimmedMuons")
#process.kinFitTtSemiLepEvent.mets = cms.InputTag("pfType1CorrectedMet")
process.kinFitTtSemiLepEvent.mets = cms.InputTag("slimmedMETs")

# The following variables are defined in :
# TopQuarkAnalysis/TopKinFitter/plugins/TtSemiLepKinFitProducer.h
process.kinFitTtSemiLepEvent.udscResolutions = udscResolutionPF.functions
process.kinFitTtSemiLepEvent.bResolutions = bjetResolutionPF.functions
process.kinFitTtSemiLepEvent.lepResolutions = muonResolution.functions
process.kinFitTtSemiLepEvent.metResolutions = metResolutionPF.functions
process.kinFitTtSemiLepEvent.metResolutions[0].eta = "9999"

'''
if not isData :
    process.kinFitTtSemiLepEvent.jetEnergyResolutionScaleFactors = cms.vdouble (
1.052, 1.057, 1.096, 1.134, 1.288  )
    process.kinFitTtSemiLepEvent.jetEnergyResolutionEtaBinning = cms.vdouble(
0.0, 0.5, 1.1, 1.7, 2.3, -1. )

    process.cleanPatJetsNominal = process.cleanPatJets.clone()
    process.cleanPatJetsNominal.src = cms.InputTag("scaledJetEnergyNominal:slimmedJets")
    process.cleanPatJetsNominal.preselection = cms.string("pt>24 && abs(eta)<2.5")
    process.kinFitTtSemiLepEvent.jets = cms.InputTag("cleanPatJetsNominal")
    process.kinFitTtSemiLepEvent.mets = cms.InputTag("scaledJetEnergyNominal:slimmedMETs")
'''


#set b-tagging in KineFit
#process.kinFitTtSemiLepEvent.bTagAlgo  = cms.string("combinedSecondaryVertexBJetTags")
process.kinFitTtSemiLepEvent.bTagAlgo  = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags")
#process.kinFitTtSemiLepEvent.bTagAlgo  = cms.string("pfCombinedSecondaryVertexV2BJetTags")
process.kinFitTtSemiLepEvent.minBDiscBJets = cms.double(0.679)
process.kinFitTtSemiLepEvent.maxBDiscLightJets = cms.double(3.0)
process.kinFitTtSemiLepEvent.useBTagging   = cms.bool(True)

#---------------------------
# Add JES Up and Down and Rerun the KineFitter
# The following variables are defined in :
# MiniTree/Utilities/python/JetEnergyScale_cfi.py
process.scaledJetEnergyUp = process.scaledJetEnergyNominal.clone()
process.scaledJetEnergyUp.inputJets = "slimmedJets"
process.scaledJetEnergyUp.inputMETs = "slimmedMETs"
process.scaledJetEnergyUp.scaleType = "jes:up"
process.cleanPatJetsJESUp = process.cleanPatJets.clone()
process.cleanPatJetsJESUp.src = cms.InputTag("slimmedJets")
#process.cleanPatJetsJESUp.src = cms.InputTag("scaledJetEnergyUp:slimmedJets")
process.cleanPatJetsJESUp.preselection = cms.string("pt>24 && abs(eta)<2.5")
process.kinFitTtSemiLepEventJESUp = process.kinFitTtSemiLepEvent.clone()
process.kinFitTtSemiLepEventJESUp.jets = cms.InputTag("slimmedJets")
#process.kinFitTtSemiLepEventJESUp.jets = cms.InputTag("cleanPatJetsJESUp")
process.kinFitTtSemiLepEventJESUp.mets = cms.InputTag("slimmedMETs")
#process.kinFitTtSemiLepEventJESUp.mets = cms.InputTag("scaledJetEnergyUp:slimmedMETs")
#---------------------------

process.scaledJetEnergyDown = process.scaledJetEnergyNominal.clone()
process.scaledJetEnergyDown.inputJets = "slimmedJets"
process.scaledJetEnergyDown.inputMETs = "slimmedMETs"
process.scaledJetEnergyDown.scaleType = "jes:down"
process.cleanPatJetsJESDown = process.cleanPatJets.clone()
process.cleanPatJetsJESDown.src = cms.InputTag("slimmedJets")
#process.cleanPatJetsJESDown.src = cms.InputTag("scaledJetEnergyDown:slimmedJets")
process.cleanPatJetsJESDown.preselection = cms.string("pt>24 && abs(eta)<2.5")
process.kinFitTtSemiLepEventJESDown = process.kinFitTtSemiLepEvent.clone()
process.kinFitTtSemiLepEventJESDown.jets = cms.InputTag("slimmedJets")
#process.kinFitTtSemiLepEventJESDown.jets = cms.InputTag("cleanPatJetsJESDown")
process.kinFitTtSemiLepEventJESDown.mets = cms.InputTag("slimmedMETs")
#process.kinFitTtSemiLepEventJESDown.mets = cms.InputTag("scaledJetEnergyDown:slimmedMETs")

# Add JER Up and Down and Rerun the KineFitter
process.scaledJetEnergyResnUp = process.scaledJetEnergyNominal.clone()
process.scaledJetEnergyResnUp.inputJets = "slimmedJets"
process.scaledJetEnergyResnUp.inputMETs = "slimmedMETs"
process.scaledJetEnergyResnUp.scaleType = "jer"
process.scaledJetEnergyResnUp.resolutionFactors = cms.vdouble(
1.115, 1.114, 1.161, 1.228, 1.488 )
process.cleanPatJetsResnUp = process.cleanPatJets.clone()
process.cleanPatJetsResnUp.src = cms.InputTag("slimmedJets")
#process.cleanPatJetsResnUp.src = cms.InputTag("scaledJetEnergyResnUp:slimmedJets")
process.cleanPatJetsResnUp.preselection = cms.string("pt>24 && abs(eta)<2.5")
process.kinFitTtSemiLepEventJERUp = process.kinFitTtSemiLepEvent.clone()
process.kinFitTtSemiLepEventJERUp.jets = cms.InputTag("slimmedJets")
#process.kinFitTtSemiLepEventJERUp.jets = cms.InputTag("cleanPatJetsResnUp")
process.kinFitTtSemiLepEventJERUp.mets = cms.InputTag("slimmedMETs")
#process.kinFitTtSemiLepEventJERUp.mets = cms.InputTag("scaledJetEnergyResnUp:slimmedMETs")

process.scaledJetEnergyResnDown = process.scaledJetEnergyNominal.clone()
process.scaledJetEnergyResnDown.inputJets = "slimmedJets"
process.scaledJetEnergyResnDown.inputMETs = "slimmedMETs"
process.scaledJetEnergyResnDown.scaleType = "jer"
process.scaledJetEnergyResnDown.resolutionFactors = cms.vdouble(
0.990, 1.001, 1.032, 1.042, 1.089 )
process.cleanPatJetsResnDown = process.cleanPatJets.clone()
process.cleanPatJetsResnDown.src = cms.InputTag("slimmedJets")
#process.cleanPatJetsResnDown.src = cms.InputTag("scaledJetEnergyResnDown:slimmedJets")
process.cleanPatJetsResnDown.preselection = cms.string("pt>24 && abs(eta)<2.5")
process.kinFitTtSemiLepEventJERDown = process.kinFitTtSemiLepEvent.clone()
process.kinFitTtSemiLepEventJERDown.jets = cms.InputTag("slimmedJets")
#process.kinFitTtSemiLepEventJERDown.jets = cms.InputTag("cleanPatJetsResnDown")
process.kinFitTtSemiLepEventJERDown.mets = cms.InputTag("slimmedMETs")
#process.kinFitTtSemiLepEventJERDown.mets = cms.InputTag("scaledJetEnergyResnDown:slimmedJets")

process.kinFitSequence = cms.Sequence(process.cleanPatJetsResCor* process.kinFitTtSemiLepEvent)

'''
if not isData :
    process.kinFitSequence.remove(process.cleanPatJetsResCor)
    process.kinFitSequence.replace(process.kinFitTtSemiLepEvent, process.scaledJetEnergyNominal * process.cleanPatJetsNominal * process.kinFitTtSemiLepEvent)
'''
'''
print "jets used in Kinematic fit", process.kinFitTtSemiLepEvent.jets
#print "jet input to cleanPatJetsResCor", process.cleanPatJetsResCor.src
'''
print "Read the KinFit cfg file ----------------"
## configure output module
process.out = cms.OutputModule("PoolOutputModule",
fileName = cms.untracked.string('ttSemiLepKinFitMuon.root'),
outputCommands = cms.untracked.vstring('drop *')
)
#process.out.outputCommands += ['keep *_kinFitTtSemiLepEvent_*_*']
process.out.outputCommands += ['keep *_kinFitTtSemiLepEvent*_*_*']
## output path
process.outpath = cms.EndPath(process.out)

