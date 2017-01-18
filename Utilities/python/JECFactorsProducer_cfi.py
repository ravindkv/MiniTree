import FWCore.ParameterSet.Config as cms

# EDProducer calls the CorrJetProducer, which is defined in CorrJetProducer.cc
resCorJet = cms.EDProducer("CorrJetProducer",
    inputJets    = cms.InputTag("patJets"),
    JECSrcFile   = cms.FileInPath("MiniTree/Utilities/data/80X_mcRun2_asymptotic_2016_miniAODv2_v1_L2L3Residual_AK4PF.txt"),
    rho          = cms.InputTag('kt6PFJets', 'rho'),
)
