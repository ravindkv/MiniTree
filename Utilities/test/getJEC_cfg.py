import FWCore.ParameterSet.Config as cms

# DOCUMENTATION : Get the JEC txt files from the database for 13TeV :
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#GetTxtFiles

process = cms.Process("jectxt")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
gt = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'
#gt = '80X_dataRun2_2016SeptRepro_v7'
process.GlobalTag.globaltag = cms.string(gt)
# define your favorite global tag
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
process.source = cms.Source("EmptySource")
process.readAK4PFchs    = cms.EDAnalyzer('JetCorrectorDBReader',
        # below is the communication to the database
        payloadName    = cms.untracked.string('AK4PFchs'),
        # this is used ONLY for the name of the printed txt files. You can use any name that you like,
        # but it is recommended to use the GT name that you retrieved the files from.
        globalTag      = cms.untracked.string(gt),
        printScreen    = cms.untracked.bool(False),
        createTextFile = cms.untracked.bool(True)
  )
process.p = cms.Path(process.readAK4PFchs)

# OUTPUT :
# After runing this code (cmsRun getJEC_cfg.py), a number of txt files will be created. The names of the txt files will have the format 80X_mcRun2_asymptotic_2016_miniAODv2_v1_XXXX_YYYY.txt, where XXXX is the correction level (e.g. L2Relative), and where YYYY is the payload name (jet algo).
# For more info about these files, see : https://twiki.cern.ch/twiki/bin/view/CMS/IntroToJEC
