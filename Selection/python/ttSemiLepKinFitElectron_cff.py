import FWCore.ParameterSet.Config as cms

from TopQuarkAnalysis.TopObjectResolutions.stringResolutions_etEtaPhi_Fall11_cff import *
from MiniTree.Utilities.JetEnergyScale_cfi import *
from MiniTree.Selection.LocalSources_cff import toPrint

def addSemiLepKinFitElectron(process, isData=False) :

    ## std sequence to produce the kinematic fit for semi-leptonic events
    process.load("TopQuarkAnalysis.TopKinFitter.TtSemiLepKinFitProducer_Electrons_cfi")
    process.load( "PhysicsTools.PatAlgos.patSequences_cff" )

    #apply selections on electron
    '''
    simpleCutsVeto = "(" + \
                     " (isEB && userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values')<0.010 && userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values')<0.80 && "+ \
                     "          userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values') <0.007 && userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values') <0.15)"   + \
                     " || "  + \
                     " (isEE && userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values')<0.030 && userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values')<0.70 && "+ \
                     "          userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values') <0.010)"   + \
                     ")"
    eleIdCutMedium = "((abs(superCluster.eta) <= 1.479 &&
    full5x5_sigmaIetaIeta <0.0115 &&
    abs(e->dEtaInSeed)      < 0.00749 &&
    deltaPhiSuperClusterTrackAtVtx <0.228 &&
    hadronicOverEm < 0.356 &&
    abs(1.0 - eSuperClusterOverP)*1/ecalEnergy < 0.299 &&
    e->nInnerHits           <= 2
    passConversionVeto

    userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values')>0.94)" + \
               " (abs(superCluster.eta) > 0.8 && abs(superCluster.eta) < 1.479 && userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values')>0.85)" + \
               " || "  + \
               " (abs(superCluster.eta) > 1.479 && userFloat('ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values')>0.92)" + \
               ")"
    process.cleanPatElectronsUser = process.cleanPatElectrons.clone()
    process.cleanPatElectronsUser.preselection = cms.string("pt>30 && abs(eta)<2.5 && "+
                                                            simpleCutsVeto +
                                                            " && " +
                                                            eleIdCut +
                                                            " && abs(userFloat('dxyWrtPV'))<0.045 && abs(userFloat('dzWrtPV'))<0.2"+
                                                            " && userFloat('nHits')==0 && userInt('antiConv')>0.5" +
                                                            " && userFloat('PFRelIso04')<0.30"
                                                            )
    '''
    #these inputs are required for cleanPatJets
    process.cleanPatMuons.src = cms.InputTag("slimmedMuons")
    process.cleanPatPhotons.src = cms.InputTag("slimmedPhotons")
    process.cleanPatTaus.src = cms.InputTag("slimmedTaus")


    #clean jets from electrons
    process.cleanPatJetsUser = process.cleanPatJets.clone()
    process.cleanPatJetsUser.checkOverlaps.electrons.src  = cms.InputTag("cleanPatElectronsUser")
    process.cleanPatJetsUser.preselection = cms.string("pt>27 && abs(eta)<2.5")
    process.cleanPatJetsUser.checkOverlaps.electrons.requireNoOverlaps  = cms.bool(True)

    #smear the JetEnergy for JER in case of MC, don't use this scaled collection for Data
    process.scaledJetEnergyNominal = scaledJetEnergy.clone()
    process.scaledJetEnergyNominal.inputJets = "cleanPatJetsUser"
    process.scaledJetEnergyNominal.inputMETs = "slimmedMETs"
    process.scaledJetEnergyNominal.scaleType = "jer"
    process.scaledJetEnergyNominal.resolutionEtaRanges = cms.vdouble(0., 0.5, 0.5, 0.8, 0.8, 1.1, 1.1, 1.3, 1.3, 1.7, 1.7, 1.9, 1.9, 2.1, 2.1, 2.3, 2.3, 2.5, 2.5, 2.8, 2.8, 3.0, 3.0, 3.2, 3.2, -1)
    process.scaledJetEnergyNominal.resolutionFactors = cms.vdouble(1.109, 1.138, 1.114, 1.123, 1.084, 1.082, 1.140, 1.067, 1.177, 1.364, 1.857, 1.328, 1.16)


    #change constraints on kineFit
    process.kinFitTtSemiLepEvent.mTop = cms.double(172.5)
    process.kinFitTtSemiLepEvent.constraints = cms.vuint32(3, 4)
    process.kinFitTtSemiLepEvent.maxNJets = cms.int32(-1)
    process.kinFitTtSemiLepEvent.udscResolutions = udscResolutionPF.functions
    process.kinFitTtSemiLepEvent.bResolutions = bjetResolutionPF.functions
    process.kinFitTtSemiLepEvent.lepResolutions = muonResolution.functions
    process.kinFitTtSemiLepEvent.metResolutions = metResolutionPF.functions
    process.kinFitTtSemiLepEvent.metResolutions[0].eta = "9999"
    process.kinFitTtSemiLepEvent.jets = cms.InputTag("cleanPatJetsUser")
    process.kinFitTtSemiLepEvent.leps = cms.InputTag("slimmedElectrons")
    process.kinFitTtSemiLepEvent.mets = cms.InputTag("slimmedMETs")

    if not isData :
        process.kinFitTtSemiLepEvent.jetEnergyResolutionEtaBinning = cms.vdouble(0., 0.5, 0.8, 1.1, 1.3, 1.7, 1.9, 2.1, 2.3, 2.5, 2.8, 3.0, 3.2, -1)
        process.kinFitTtSemiLepEvent.jetEnergyResolutionScaleFactors = cms.vdouble(1.109, 1.138, 1.114, 1.123, 1.084, 1.082, 1.140, 1.067, 1.177, 1.364, 1.857, 1.328, 1.16)
        process.cleanPatJetsNominal.src = cms.InputTag("scaledJetEnergyNominal:cleanPatJetsUser")
        process.cleanPatJetsNominal.preselection = cms.string("pt>27 && abs(eta)<2.5")
        process.kinFitTtSemiLepEvent.jets = cms.InputTag("cleanPatJetsNominal")
        process.kinFitTtSemiLepEvent.mets = cms.InputTag("scaledJetEnergyNominal:slimmedMETs")

    #set b-tagging in KineFit
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
    process.kinFitTtSemiLepEvent.bTagAlgo = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags")
    process.kinFitTtSemiLepEvent.minBDiscBJets= cms.double(0.5426)
    #process.kinFitTtSemiLepEvent.minBDiscBJets= cms.double(0.8484)
    #process.kinFitTtSemiLepEvent.minBDiscBJets= cms.double(0.9535)
    process.kinFitTtSemiLepEvent.maxBDiscLightJets = cms.double(3.0)
    process.kinFitTtSemiLepEvent.useBTagging  = cms.bool(True)

    # Add JES Up and Down and Rerun the KineFitter
    # JESUp
    process.scaledJetEnergyUp = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyUp.inputJets = "cleanPatJetsUser"
    process.scaledJetEnergyUp.inputMETs = "slimmedMETs"
    process.scaledJetEnergyUp.scaleType = "jes:up"
    process.cleanPatJetsJESUp = process.cleanPatJets.clone()
    process.cleanPatJetsJESUp.src = cms.InputTag("scaledJetEnergyUp:cleanPatJetsUser")
    process.cleanPatJetsJESUp.preselection = cms.string("pt>27 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJESUp = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJESUp.jets = cms.InputTag("cleanPatJetsJESUp")
    process.kinFitTtSemiLepEventJESUp.mets = cms.InputTag("scaledJetEnergyUp:slimmedMETs")

    # JESDown
    process.scaledJetEnergyDown = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyDown.inputJets = "cleanPatJetsUser"
    process.scaledJetEnergyDown.inputMETs = "slimmedMETs"
    process.scaledJetEnergyDown.scaleType = "jes:down"
    process.cleanPatJetsJESDown = process.cleanPatJets.clone()
    process.cleanPatJetsJESDown.src = cms.InputTag("scaledJetEnergyDown:cleanPatJetsUser")
    process.cleanPatJetsJESDown.preselection = cms.string("pt>27 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJESDown = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJESDown.jets = cms.InputTag("cleanPatJetsJESDown")
    process.kinFitTtSemiLepEventJESDown.mets = cms.InputTag("scaledJetEnergyDown:slimmedMETs")

    # Add JER Up and Down and Rerun the KineFitter
    # JERUp
    process.scaledJetEnergyResnUp = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyResnUp.inputJets = "cleanPatJetsUser"
    process.scaledJetEnergyResnUp.inputMETs = "slimmedMETs"
    process.scaledJetEnergyResnUp.scaleType = "jer"
    process.scaledJetEnergyResnUp.resolutionFactors = cms.vdouble(1.109, 1.138, 1.114, 1.123, 1.084, 1.082, 1.140, 1.067, 1.177, 1.364, 1.857, 1.328, 1.16)
    process.cleanPatJetsResnUp = process.cleanPatJets.clone()
    process.cleanPatJetsResnUp.src = cms.InputTag("scaledJetEnergyResnUp:cleanPatJetsUser")
    process.cleanPatJetsResnUp.preselection = cms.string("pt>27 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJERUp = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJERUp.jets = cms.InputTag("cleanPatJetsResnUp")
    process.kinFitTtSemiLepEventJERUp.mets = cms.InputTag("scaledJetEnergyResnUp:slimmedMETs")

    # JERDown
    process.scaledJetEnergyResnDown = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyResnDown.inputJets = "cleanPatJetsUser"
    process.scaledJetEnergyResnDown.inputMETs = "slimmedMETs"
    process.scaledJetEnergyResnDown.scaleType = "jer"
    process.scaledJetEnergyResnDown.resolutionFactors = cms.vdouble(1.109, 1.138, 1.114, 1.123, 1.084, 1.082, 1.140, 1.067, 1.177, 1.364, 1.857, 1.328, 1.16)
    process.cleanPatJetsResnDown = process.cleanPatJets.clone()
    process.cleanPatJetsResnDown.src = cms.InputTag("scaledJetEnergyResnDown:cleanPatJetsUser")
    process.cleanPatJetsResnDown.preselection = cms.string("pt>27 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJERDown = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJERDown.jets = cms.InputTag("cleanPatJetsResnDown")
    process.kinFitTtSemiLepEventJERDown.mets = cms.InputTag("scaledJetEnergyResnDown:slimmedMETs")

    #Put them in a sequence
    process.kinFitSequence = cms.Sequence(process.cleanPatMuons*
            process.cleanPatElectrons*
            process.cleanPatPhotons*
            process.cleanPatTaus*
            process.cleanPatJetsUser*
            process.scaledJetEnergyNominal *
            process.cleanPatJetsNominal *
            process.kinFitTtSemiLepEvent *
            process.scaledJetEnergyUp *
            process.cleanPatJetsJESUp *
            process.kinFitTtSemiLepEventJESUp *
            process.scaledJetEnergyDown *
            process.cleanPatJetsJESDown *
            process.kinFitTtSemiLepEventJESDown *
            process.scaledJetEnergyResnUp *
            process.cleanPatJetsResnUp *
            process.kinFitTtSemiLepEventJERUp *
            process.scaledJetEnergyResnDown *
            process.cleanPatJetsResnDown *
            process.kinFitTtSemiLepEventJERDown)
    toPrint("jets used in Kinematic fit", process.kinFitTtSemiLepEvent.jets)

