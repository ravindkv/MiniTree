
import FWCore.ParameterSet.Config as cms

from MiniTree.Selection.LocalRunSkeleton_cff import *
from MiniTree.Selection.ttSemiLepKinFitElectron_cff import *

process.maxEvents.input = cms.untracked.int32(10)
process.TFileService.fileName = cms.string('ntuple_13TeV_Electrons.root')
#process.TFileService.fileName = cms.string('mc_muon_5th_Aug_2014.root')

# config parameters ------------------------------------------------------------
procName='LOCALUSER'
process.source.fileNames = ["/store/mc/RunIISpring16MiniAODv1/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FED53EE4-7D16-E611-AE17-B083FED406AD.root"]

trigMenu = 'HLT'
isData=False
isAOD=True
isFastsim = False
#mutriglist = [ 'HLT_Mu15_v2' ]
mutriglist = [ 'HLT_IsoMu24_eta2p1_v8' ]
#egtriglist = [ 'HLT_Ele27_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_v2']
egtriglist = [ 'HLT_Ele27_WP80_v8','HLT_Ele27_WP80_v9', 'HLT_Ele27_WP80_v10','HLT_Ele27_WP80_v11']
#HLT_Ele27_WP80_v
jettriglist = [ 'HLT_Jet30_v1' ]
trigpath = ''
applyResJEC=False
addPF2PAT=False
storeOutPath=False
#channel = electron

# start process configuration -------------------------------------------------
process.setName_(procName)
producePDFweights=False
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag  = cms.string('80X_mcRun2_asymptotic_2016_miniAODv2_v1')

# configure the extra modules -------------------------------------------------
if(addPF2PAT):
    print "**** Adding PF2PAT objects ****"
    addpf2PatSequence(process, not isData)
defineBasePreSelection(process,False,not isFastsim and not isAOD)

#configureTauProduction(process, not isData)
#addJetMETExtra(process,isData,applyResJEC,isAOD)
#addTriggerMatchExtra(process,egtriglist,mutriglist,jettriglist,False,trigMenu)
#defineGenUtilitiesSequence(process)
#configureElectronMVAIdIso(process)
addSemiLepKinFitElectron(process, isData)

# add the analysis modules ----------------------------------------------------
process.load('MiniTree.Selection.selection_cfi')
process.myMiniTreeProducer.MCTruth.isData = cms.bool(isData)
process.myMiniTreeProducer.MCTruth.sampleCode = cms.string('TTBAR')
process.myMiniTreeProducer.MCTruth.producePDFweights = cms.bool(producePDFweights)
#process.myMiniTreeProducer.Taus.sources = cms.VInputTag("patTaus", "patTausPFlow")
process.myMiniTreeProducer.minEventQualityToStore = cms.int32(0)
process.myMiniTreeProducer.Trigger.source = cms.InputTag('TriggerResults::'+trigMenu)
process.myMiniTreeProducer.Trigger.bits = cms.vstring()
process.myMiniTreeProducer.Trigger.bits = mutriglist
process.myMiniTreeProducer.Trigger.bits.extend( egtriglist )
process.myMiniTreeProducer.Trigger.bits.extend( jettriglist )
process.myMiniTreeProducer.MCTruth.sampleChannel = cms.string('electron')
#process.myMiniTreeProducer.MCTruth.sampleChannel = cms.string('muon')
#process.myMiniTreeProducer.KineFit.runKineFitter = cms.bool(False)
########################################################

# analysis sequence ------------------------------------------------------------
##process.met_extra = cms.Path(process.RecoMetSequence * process.patPfMetT0pcT1Txy)
process.kineFit = cms.Path(process.kinFitSequence) #cms.Path(process.kinFitTtSemiLepEvent)
##process.ele_extra = cms.Path(process.mvaID + process.pfIsolationSequence)
##process.ele_embed = cms.Path(process.EleEmbedSequence)

process.p  = cms.Path(process.allEventsFilter*process.basePreSel*process.myMiniTreeProducer)
#process.p  = cms.Path( process.basePreSel*process.myMiniTreeProducer)
'''
if( addPF2PAT ):
    process.pat_default = cms.Path( process.patSequence * process.patDefaultSequence * process.puJetIdSqeuence)
else :
    process.pat_default = cms.Path( process.patDefaultSequence * process.puJetIdSqeuence)
'''
process.schedule = cms.Schedule(process.kineFit, process.p)
##process.schedule = cms.Schedule(process.ele_extra, process.pat_default, process.met_extra, process.ele_embed, process.kineFit, process.p)

checkProcessSchedule(storeOutPath,True)

if(isAOD) :
    print " "
    print "////////////////////////////////////////////////////////////////////////"
    print "//                   This is AOD run                                  //"
    print "//                                                                    //"
    print "////////////////////////////////////////////////////////////////////////"
    print " "

    from PhysicsTools.PatAlgos.tools.coreTools import *
    #restrictInputToAOD(process)
    process.myMiniTreeProducer.Electrons.ebRecHits = cms.InputTag("reducedEcalRecHitsEB")
    process.myMiniTreeProducer.Electrons.eeRecHits = cms.InputTag("reducedEcalRecHitsEE")
