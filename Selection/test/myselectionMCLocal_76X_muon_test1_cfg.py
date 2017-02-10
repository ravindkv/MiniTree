
import FWCore.ParameterSet.Config as cms

## CMSSW_7_6_3/src/MiniTree/Selection/python
from MiniTree.Selection.LocalRunSkeleton_cff import *
from MiniTree.Selection.ttSemiLepKinFitMuon_cff import *

process.maxEvents.input = cms.untracked.int32(1000)
process.TFileService.fileName = cms.string('bb.root')

# config parameters ------------------------------------------------------------
procName='LOCALUSER'
#process.source.fileNames = ["file:TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_MINIAODSIM.root"]
#process.source.fileNames = ["/store/mc/RunIISpring16MiniAODv2/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/FEDED4C8-573B-E611-9ED6-0025904CF102.root"]
#process.source.fileNames = ["file:/afs/cern.ch/work/r/rverma/private/genProd_13TeV_signal/local_genProd/CMSSW_7_1_20/src/root_files/mini_AODSIM.root"]
process.source.fileNames = ["/store/mc/RunIISpring16MiniAODv1/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FED53EE4-7D16-E611-AE17-B083FED406AD.root"]
#process.source.fileNames = ["/store/mc/RunIISpring15FSPremix/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/10000/0036D0D2-BC5F-E511-AEEB-00259073E4BE.root"]
#process.source.fileNames = ["/store/mc/RunIIFall15MiniAODv2/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/00D010B5-1EB9-E511-B950-02163E014965.root"]
#process.source.fileNames = ["file:/tmp/gkole/TT_CT10_8TeV_powheg-04731110-2815-E211-9DE4-0017A4770008.root"]
#process.source.fileNames = ["/store/relval/CMSSW_7_6_3_patch2/RelValTTbar_13/MINIAODSIM/PUpmx25ns_76X_mcRun2_asymptotic_v12-v1/10000/2ACA73CD-1BE0-E511-8BB6-0CC47A78A458.root"]
#fileNames = cms.untracked.vstring('/store/mc/RunIIFall15MiniAODv2/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/00D010B5-1EB9-E511-B950-02163E014965.root')

trigMenu = 'HLT'
isData=False
isAOD=False
isFastsim = False
mutriglist = [ 'HLT_Mu15_v2' ]
#mutriglist = [ 'HLT_IsoMu27_v3' ]
#egtriglist = [ 'HLT_Ele27_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_v2']
egtriglist = [ 'HLT_Ele27_eta2p1_WPLoose_Gsf_v2']
#HLT_Ele27_WP80_v
#jettriglist = [ 'HLT_Jet30_v1' ]
jettriglist = [ 'HLT_JetE30_NoBPTX_v2' ]
trigpath = ''
applyResJEC=False
addPF2PAT=False
storeOutPath=False
filterHBHEnoise = False
#channel = electron

# start process configuration -------------------------------------------------
process.setName_(procName)
producePDFweights=False
#process.GlobalTag.globaltag = cms.string( 'START53_V15::All' )
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
#process.GlobalTag.globaltag  = cms.string('76X_mcRun2_asymptotic_RunIIFall15DR76_v1')
process.GlobalTag.globaltag  = cms.string('80X_mcRun2_asymptotic_2016_miniAODv2_v1')


# configure the extra modules -------------------------------------------------
if(addPF2PAT):
    print "**** Adding PF2PAT objects ****"
    addpf2PatSequence(process, not isData)
defineBasePreSelection(process,False, False)

#configureTauProduction(process, not isData)
addJetMETExtra(process,isData,applyResJEC,isAOD)
addTriggerMatchExtra(process,egtriglist,mutriglist,jettriglist,False,trigMenu)
defineGenUtilitiesSequence(process)
#configureElectronMVAIdIso(process)
addSemiLepKinFitMuon(process, isData) #important


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
#process.myMiniTreeProducer.MCTruth.sampleChannel = cms.string('electron')
process.myMiniTreeProducer.MCTruth.sampleChannel = cms.string('muon')
#process.myMiniTreeProducer.KineFit.runKineFitter = cms.bool(False)
process.myMiniTreeProducer.KineFit.runKineFitter = cms.bool(False)
########################################################


# analysis sequence ------------------------------------------------------------
process.met_extra = cms.Path(process.RecoMetSequence * process.patPfMetT0pcT1Txy)
process.kineFit = cms.Path(process.kinFitSequence) #cms.Path(process.kinFitTtSemiLepEvent) #important
#process.ele_extra = cms.Path(process.mvaID + process.pfIsolationSequence)
#process.ele_embed = cms.Path(process.EleEmbedSequence)


process.p  = cms.Path(process.allEventsFilter*process.basePreSel*process.myMiniTreeProducer)

# checking
#process.schedule = cms.Schedule( process.kineFit, process.p)
#process.schedule = cms.Schedule(process.p, process.kineFit)
#process.schedule = cms.Schedule(process.p)


#process.p  = cms.Path( process.basePreSel*process.myMiniTreeProducer)

#if( addPF2PAT ):
#    process.pat_default = cms.Path( process.patSequence * process.patDefaultSequence * process.puJetIdSqeuence)
#else :
#    process.pat_default = cms.Path( process.patDefaultSequence * process.puJetIdSqeuence)

#process.schedule = cms.Schedule(process.ele_extra, process.pat_default, process.met_extra, process.ele_embed, process.kineFit, process.p)

#process.schedule = cms.Schedule(process.met_extra, process.kineFit, process.p)
process.schedule = cms.Schedule(process.kineFit, process.p)

#process.schedule = cms.Schedule(process.met_extra, process.p) #important

checkProcessSchedule(storeOutPath,True)

#if(isAOD) :
#    print "**** This is AOD run ****"
#    from PhysicsTools.PatAlgos.tools.coreTools import *
#    restrictInputToAOD(process)
#    process.myMiniTreeProducer.Electrons.ebRecHits = cms.InputTag("reducedEcalRecHitsEB")
#    process.myMiniTreeProducer.Electrons.eeRecHits = cms.InputTag("reducedEcalRecHitsEE")
