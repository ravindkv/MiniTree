import FWCore.ParameterSet.Config as cms

#------------------------------------------------------
# The process object
#------------------------------------------------------
process = cms.Process('MiniTree')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True))
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100


#------------------------------------------------------
# Import other attributes and functions
#------------------------------------------------------
from MiniTree.Selection.JetMETExtra_cff import *
from MiniTree.Selection.ElectronExtra_cff import *
from MiniTree.Selection.ttSemiLepKinFitElectron_cff import *


#------------------------------------------------------
# User flags
#------------------------------------------------------
isData=False


#------------------------------------------------------
# Input root files and number of events
#------------------------------------------------------
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('/store/data/Run2016C/SingleElectron/MINIAOD/03Feb2017-v1/100000/02169BE7-81EB-E611-BB99-02163E0137CD.root')
    fileNames = cms.untracked.vstring("/store/mc/RunIISummer16MiniAODv2/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0693E0E7-97BE-E611-B32F-0CC47A78A3D8.root")
    #fileNames = cms.untracked.vstring('file:0693E0E7-97BE-E611-B32F-0CC47A78A3D8.root')
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))


#------------------------------------------------------
# Output file
#------------------------------------------------------
process.load("PhysicsTools.UtilAlgos.TFileService_cfi")
process.TFileService.fileName = cms.string("outFile_.root")
# WARNING: Don't change name of the outfile (outFile_.root)
#as it is used in the MultiCRAB package for job submission


#------------------------------------------------------
# Global tags
#------------------------------------------------------
trigMenu = 'HLT'
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag  = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v8')
if isData:
    process.GlobalTag.globaltag  = cms.string('80X_dataRun2_2016SeptRepro_v7')


#------------------------------------------------------
# Inputs for MiniTree EDAnalyser
#------------------------------------------------------
process.load('MiniTree.Selection.EventSelectors_cfi')
# sample type
process.myMiniTreeProducer.MCTruth.isData = cms.bool(isData)
process.myMiniTreeProducer.MCTruth.sampleChannel = cms.string('electron')
if isData:
    process.myMiniTreeProducer.MCTruth.sampleCode = cms.string("DATA")
else:
    process.myMiniTreeProducer.MCTruth.sampleCode = cms.string("sampCode_")
    # WARNING: Don't change name of the sampleCode (sampleCode_)
    #as it is used in the MultiCRAB package for job submission
# triggers
process.myMiniTreeProducer.Trigger.source = cms.InputTag('TriggerResults::'+trigMenu)
process.myMiniTreeProducer.Trigger.trigBits = cms.vstring("HLT_Ele27_WPTight_Gsf")


#------------------------------------------------------
# apply partial MET filters via trigger selection.
# BadPFMuonFilter and BadChargedCandidateFilter are
# run on fly through addMETFilters (process)
#------------------------------------------------------
addMETFilters(process)
process.myMiniTreeProducer.Trigger.sourceFilter = cms.InputTag('TriggerResults')
process.myMiniTreeProducer.Trigger.metFilterBits = cms.vstring("Flag_goodVertices",
"Flag_globalSuperTightHalo2016Filter",
"Flag_HBHENoiseFilter",
"Flag_HBHENoiseIsoFilter",
"Flag_EcalDeadCellTriggerPrimitiveFilter"
)
if(isData):
    process.myMiniTreeProducer.Trigger.metFilterBits.extend(["Flag_eeBadScFilter"])

# Apply L1L2L3 corrections on jet
addCorrJetL1L2L3(process, isData)


#------------------------------------------------------
# KinFit and jet energy/pT reso
#------------------------------------------------------
addSemiLepKinFitElectron(process, isData)
configureElectronCutIdIso(process)
process.myMiniTreeProducer.KineFit.runKineFitter = cms.bool(True)
process.myMiniTreeProducer.Jets.resolutionsFile = cms.string('Spring16_25nsV10_MC_PtResolution_AK4PF.txt')
process.myMiniTreeProducer.Jets.scaleFactorsFile = cms.string('Spring16_25nsV10_MC_SF_AK4PF.txt')


#------------------------------------------------------
# Events to be stored in the ntuple after which cut
# 1 = after trigger selection
#------------------------------------------------------
process.myMiniTreeProducer.minEventQualityToStore = cms.int32(1)


#------------------------------------------------------
# Add ED Filters, Producers, Analysers in the cms Path
#------------------------------------------------------
process.p  = cms.Path(process.allEventsFilter*
        process.metFilterSequence*
        #process.corrJetsProducerSequence*
        process.EleEmbedSequence*
        process.kinFitSequence*
        process.myMiniTreeProducer)
process.schedule = cms.Schedule(process.p)
