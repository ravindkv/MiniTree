import FWCore.ParameterSet.Config as cms

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

## define input
#from TopQuarkAnalysis.TopEventProducers.tqafInputFiles_cff import relValTTbar
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIISpring16MiniAODv1/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FED53EE4-7D16-E611-AE17-B083FED406AD.root')
)

## define maximal number of events to loop over
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)

)
## configure process options
process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
    #wantSummary      = cms.untracked.bool(True)
)

## configure geometry & conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.load("Configuration.StandardSequences.MagneticField_cff")

## std sequence for PAT
#process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
#process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

## std sequence to produce the kinematic fit for semi-leptonic events
process.load("TopQuarkAnalysis.TopKinFitter.TtSemiLepKinFitProducer_Muons_cfi")
process.kinFitTtSemiLepEvent.constraints = [1,2]
process.kinFitTtSemiLepEvent.jets=cms.InputTag('slimmedJets')
process.kinFitTtSemiLepEvent.leps=cms.InputTag('slimmedMuons')
process.kinFitTtSemiLepEvent.mets=cms.InputTag('slimmedMETs')

#change constraints on kineFit
process.kinFitTtSemiLepEvent.mTop = cms.double(172.5)
#process.kinFitTtSemiLepEvent.constraints = cms.vuint32(3, 4)
#process.kinFitTtSemiLepEvent.maxNJets = cms.int32(-1)

## use object resolutions from a specific config file
'''
from TopQuarkAnalysis.TopObjectResolutions.stringResolutions_etEtaPhi_Summer11_cff import *
process.kinFitTtSemiLepEvent.udscResolutions = udscResolutionPF.functions
process.kinFitTtSemiLepEvent.bResolutions    = bjetResolutionPF.functions
process.kinFitTtSemiLepEvent.lepResolutions  = muonResolution  .functions
process.kinFitTtSemiLepEvent.metResolutions  = metResolutionPF .functions
process.kinFitTtSemiLepEvent.metResolutions[0].eta = "9999"
'''
######################## set b-tagging in KineFit
process.kinFitTtSemiLepEvent.bTagAlgo = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags")
#process.kinFitTtSemiLepEvent.minBDiscBJets = cms.double(0.079)
process.kinFitTtSemiLepEvent.minBDiscBJets = cms.double(0.0)
process.kinFitTtSemiLepEvent.maxBDiscLightJets = cms.double(3.0)
process.kinFitTtSemiLepEvent.useBTagging  = cms.bool(True)

## configure output module
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('ttSemiLepKinFitProducer.root'),
    outputCommands = cms.untracked.vstring('drop *')
)
process.out.outputCommands += ['keep *_kinFitTtSemiLepEvent*_*_*']
#process.out.outputCommands += ['keep *']

## output path
process.outpath = cms.EndPath(process.out)


