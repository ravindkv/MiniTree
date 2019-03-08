import FWCore.ParameterSet.Config as cms

#------------------------------------------------------
# Import other attributes and functions
#------------------------------------------------------
from MiniTree.Selection.LocalRunSkeleton_cff import *
from MiniTree.Selection.ttSemiLepKinFitMuon_cff import *
from MiniTree.Selection.LocalSources_cff import toPrint

#------------------------------------------------------
# User flags
#------------------------------------------------------
isData=False
applyResJEC=False
storeOutPath=False
filterHBHEnoise = False
producePDFweights=False
isAOD = False

#------------------------------------------------------
# Input root files and number of events
#------------------------------------------------------
process.maxEvents.input = cms.untracked.int32(1000)
# Data
#inFile = "/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/02973E99-69EC-E611-9913-5065F381A2F1.root"
#MC
inFile = cms.untracked.vstring("file:0693E0E7-97BE-E611-B32F-0CC47A78A3D8.root")
#inFile = "/store/mc/RunIISummer16MiniAODv2/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0693E0E7-97BE-E611-B32F-0CC47A78A3D8.root"
process.source.fileNames = inFile
#process.source.fileNames = [inFile]

#------------------------------------------------------
# Output file
#------------------------------------------------------
process.TFileService.fileName = cms.string("outFile_.root")
# WARNING: Don't change name of the outfile (outFile_.root)
#as it is used in the MultiCRAB package for job submission

#------------------------------------------------------
# Process name and GT
#------------------------------------------------------
trigMenu = 'HLT'
process.setName_('LOCALUSER')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag  = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v6')

#------------------------------------------------------
# Other modules
#------------------------------------------------------
#addTriggerMatchExtra(process,egtriglist,mutriglist,jettriglist,False,trigMenu)
defineBasePreSelection(process,False, False)
defineGenUtilitiesSequence(process)
#configureElectronMVAIdIso(process)

#------------------------------------------------------
# Inputs for MiniTree EDAnalyser
#------------------------------------------------------
process.load('MiniTree.Selection.selection_cfi')
# sample type
process.myMiniTreeProducer.MCTruth.isData = cms.bool(isData)
process.myMiniTreeProducer.MCTruth.sampleChannel = cms.string('muon')
if isData:
    process.myMiniTreeProducer.MCTruth.sampleCode = cms.string("DATA")
else:
    process.myMiniTreeProducer.MCTruth.sampleCode = cms.string("sampCode_")
    # WARNING: Don't change name of the sampleCode (sampleCode_)
    #as it is used in the MultiCRAB package for job submission
process.myMiniTreeProducer.MCTruth.producePDFweights = cms.bool(producePDFweights)
# triggers
process.myMiniTreeProducer.Trigger.source = cms.InputTag('TriggerResults::'+trigMenu)
process.myMiniTreeProducer.Trigger.trigBits = cms.vstring("HLT_IsoMu24","HLT_IsoTkMu24"
)

#------------------------------------------------------
# apply MET filters via trigger selection
#------------------------------------------------------
addMETFilters(process)
process.myMiniTreeProducer.Trigger.sourceFilter = cms.InputTag('TriggerResults')
process.myMiniTreeProducer.Trigger.metFilterBits = cms.vstring("Flag_goodVertices",
"Flag_globalSuperTightHalo2016Filter",
"Flag_HBHENoiseFilter",
"Flag_HBHENoiseIsoFilter",
"Flag_EcalDeadCellTriggerPrimitiveFilter",
"Flag_BadPFMuonFilter",
"Flag_BadChargedCandidateFilter",
"Flag_ecalBadCalibFilter",
"Flag_CSCTightHalo2015Filter",
"Flag_globalSuperTightHalo2016Filter",
"Flag_globalSuperTightHalo2016Filter"
)
if(isData):
    process.myMiniTreeProducer.Trigger.metFilterBits.extend("Flag_eeBadScFilter")

#------------------------------------------------------
# KinFit and jet energy/pT reso
#------------------------------------------------------
addSemiLepKinFitMuon(process, isData)
process.myMiniTreeProducer.KineFit.runKineFitter = cms.bool(True)
process.myMiniTreeProducer.Jets.resolutionsFile = cms.string('Spring16_25nsV10_MC_PtResolution_AK4PF.txt')
process.myMiniTreeProducer.Jets.scaleFactorsFile = cms.string('Spring16_25nsV10_MC_SF_AK4PF.txt')

#------------------------------------------------------
# Events to be stored in the ntuples after which cut
# 1 = after trigger
# 2 = one lepton selection
# 3 = met selection etc
#------------------------------------------------------
process.myMiniTreeProducer.minEventQualityToStore = cms.int32(1)

#------------------------------------------------------
# Add ED Filters, Producers, Analysers in the cms Path
#------------------------------------------------------
process.p  = cms.Path(process.metFilterSequence*
        process.kinFitSequence*
        process.allEventsFilter*
        process.basePreSel*
        process.myMiniTreeProducer)
process.schedule = cms.Schedule(process.p)
checkProcessSchedule(storeOutPath,True)

