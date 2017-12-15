import FWCore.ParameterSet.Config as cms
from MiniTree.Selection.LocalRunSkeleton_cff import *
from MiniTree.Selection.ttSemiLepKinFitElectron_cff import *
from MiniTree.Selection.LocalSources_cff import toPrint

#-----------------------------------------
#INPUT & OUTPUT
#-----------------------------------------
isData=False
#inFile = "/store/data/Run2016C/SingleElectron/MINIAOD/03Feb2017-v1/100000/02169BE7-81EB-E611-BB99-02163E0137CD.root"
#inFile = "/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/02973E99-69EC-E611-9913-5065F381A2F1.root"

#inFile = ["file:FEDED4C8-573B-E611-9ED6-0025904CF102.root"]
#POWHEG TT Jets
inFile = "/store/mc/RunIISummer16MiniAODv2/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0693E0E7-97BE-E611-B32F-0CC47A78A3D8.root"

process.source.fileNames = [inFile]
process.maxEvents.input = cms.untracked.int32(-1)

#OUTPUT FILE
import datetime
date = datetime.date.today()
samp_code = inFile.split("/")[4].split("_")[0]
outFile = samp_code+"_ntuple_"+str(date)+"_electron.root"
#process.TFileService.fileName = cms.string(outFile)
#for multi CRAB
process.TFileService.fileName = cms.string("outFile_.root")

#-----------------------------------------
#CONFIG PARAMETERS
#-----------------------------------------
procName='LOCALUSER'
#trigMenu = 'HLT2' #https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD
trigMenu = 'HLT'
isFastsim = False
trigpath = ''
#Extra modules
applyResJEC=False
addPF2PAT=False
storeOutPath=False
filterHBHEnoise = False
producePDFweights=False
isAOD = False

#-----------------------------------------
#START PROCESS CONFIGURATION
#-----------------------------------------
process.setName_(procName)
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag  = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v6')

#-----------------------------------------
#CUT BASED ELECTRON ID
#-----------------------------------------
'''
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
#https://github.com/ikrav/EgammaWork/blob/ntupler_and_VID_demos_8.0.3/ElectronNtupler/     test/runElectrons_VID_CutBased_Summer16_80X_demo.py
dataFormat = DataFormat.MiniAOD
switchOnVIDElectronIdProducer(process, dataFormat)
#define which IDs we want to produce
my_id='RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff'
#add them to the VID producer
setupAllVIDIdsInModule(process,my_id,setupVIDElectronSelection)
'''
#-----------------------------------------
#CONFIGURE THE EXTRA MODULE
#-----------------------------------------
if(addPF2PAT):
    toPrint("Adding PF2PAT objects","")
    addpf2PatSequence(process, not isData)
defineBasePreSelection(process,False, False)

#configureTauProduction(process, not isData)
#addJetMETExtra(process,isData,applyResJEC,isAOD)
#addTriggerMatchExtra(process,egtriglist,mutriglist,jettriglist,False,trigMenu)
defineGenUtilitiesSequence(process)
configureElectronCutIdIso(process)
#configureElectronMVAIdIso(process)
addSemiLepKinFitElectron(process, isData) #important

#-----------------------------------------
#ADD THE ANALYSIS MODULE
#-----------------------------------------
process.load('MiniTree.Selection.selection_cfi')
process.myMiniTreeProducer.MCTruth.isData = cms.bool(isData)
if isData:
    process.myMiniTreeProducer.MCTruth.sampleCode = cms.string("DATA")
else:
    #process.myMiniTreeProducer.MCTruth.sampleCode = cms.string(samp_code)
    #for multi CRAB
    process.myMiniTreeProducer.MCTruth.sampleCode = cms.string("sampCode_")
process.myMiniTreeProducer.MCTruth.producePDFweights = cms.bool(producePDFweights)
process.myMiniTreeProducer.minEventQualityToStore = cms.int32(1)
process.myMiniTreeProducer.Trigger.source = cms.InputTag('TriggerResults::'+trigMenu)
#process.myMiniTreeProducer.Trigger.bits = cms.vstring()
#process.myMiniTreeProducer.Trigger.bits = mutriglist
#process.myMiniTreeProducer.Trigger.bits.extend( egtriglist )
#process.myMiniTreeProducer.Trigger.bits.extend( jettriglist )
process.myMiniTreeProducer.Trigger.myTrig = "HLT_Ele2"

process.myMiniTreeProducer.KineFit.runKineFitter = cms.bool(True)
process.myMiniTreeProducer.MCTruth.sampleChannel = cms.string('electron')
process.myMiniTreeProducer.Jets.resolutionsFile = cms.string('Spring16_25nsV10_MC_PtResolution_AK4PF.txt')
process.myMiniTreeProducer.Jets.scaleFactorsFile = cms.string('Spring16_25nsV10_MC_SF_AK4PF.txt')

#-----------------------------------------
#ANALYSIS SEQUENCE
#-----------------------------------------
#Run without the KinFit
#process.p  = cms.Path(process.EleEmbedSequence*process.allEventsFilter*process.basePreSel*process.myMiniTreeProducer)
#process.p  = cms.Path(process.allEventsFilter*process.basePreSel*process.myMiniTreeProducer)
#Run with the KinFit
process.p  = cms.Path(process.EleEmbedSequence*process.kinFitSequence*process.allEventsFilter*process.basePreSel*process.myMiniTreeProducer)
process.schedule = cms.Schedule(process.p)
checkProcessSchedule(storeOutPath,True)

#-----------------------------------------
#BACKUP
#-----------------------------------------
#Trigger list : http://fwyzard.web.cern.ch/fwyzard/hlt/2016/summary
'''
mutriglist =  ['HLT_IsoMu24_v1',
               'HLT_IsoMu24_v2',
               'HLT_IsoMu24_v4',
               'HLT_IsoMu27_v3',
               'HLT_IsoMu27_v4',
               'HLT_IsoMu27_v5',
               'HLT_IsoMu27_v7']

egtriglist =  ['HLT_Ele27_WPTight_Gsf_v1',
               'HLT_Ele27_WPTight_Gsf_v2',
               'HLT_Ele27_WPTight_Gsf_v3',
               'HLT_Ele27_WPTight_Gsf_v4',
               'HLT_Ele27_WPTight_Gsf_v5',
               'HLT_Ele27_WPTight_Gsf_v6',
               'HLT_Ele27_WPTight_Gsf_v7',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v2',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v3',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v4',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v5',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v6',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v7',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v8']

jettriglist = ['HLT_JetE30_NoBPTX_v2',
               'HLT_JetE30_NoBPTX_v3',
               'HLT_JetE30_NoBPTX_v4']
'''
