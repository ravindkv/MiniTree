import FWCore.ParameterSet.Config as cms

from TopQuarkAnalysis.TopObjectResolutions.stringResolutions_etEtaPhi_Fall11_cff import *
from MiniTree.Utilities.JetEnergyScale_cfi import *
from MiniTree.Selection.LocalSources_cff import toPrint

def addSemiLepKinFitElectron(process, isData=False) :

    ## std sequence to produce the kinematic fit for semi-leptonic events
    process.load("TopQuarkAnalysis.TopKinFitter.TtSemiLepKinFitProducer_Electrons_cfi")
    process.load( "PhysicsTools.PatAlgos.patSequences_cff" )

    #apply selections on electron
    process.cleanPatElectronsUser = process.cleanPatElectrons.clone()
    #process.cleanPatElectronsUser.src = cms.InputTag("slimmedElectrons")
    process.cleanPatElectronsUser.src = cms.InputTag("selectedPatElectronsUserEmbedded")
    process.cleanPatElectronsUser.preselection = cms.string("pt>25 && abs(eta)<2.5 && abs(userFloat('dxyWrtPV'))<0.05 && abs(userFloat('dzWrtPV'))<0.2 && userInt('cutBasedID')>0 && userFloat('PFRelIso04')<0.30")

    #these inputs are required for cleanPatJets
    process.cleanPatMuons.src = cms.InputTag("slimmedMuons")
    process.cleanPatPhotons.src = cms.InputTag("slimmedPhotons")
    process.cleanPatPhotons.checkOverlaps.electrons.src = cms.InputTag("cleanPatElectronsUser")
    process.cleanPatTaus.src = cms.InputTag("slimmedTaus")
    process.cleanPatTaus.checkOverlaps.electrons.src = cms.InputTag("cleanPatElectronsUser")

    #clean jets from leptons
    process.cleanPatJets.src = cms.InputTag("updatedPatJetsUpdatedJEC")
    process.cleanPatJets.preselection = cms.string("pt>20 && abs(eta)<2.5")
    process.cleanPatJets.checkOverlaps.electrons.src  = cms.InputTag("cleanPatElectronsUser")
    process.cleanPatJets.checkOverlaps.tkIsoElectrons.src  = cms.InputTag("cleanPatElectronsUser")
    process.cleanPatJets.checkOverlaps.electrons.requireNoOverlaps  = cms.bool(True)

    #smear the JetEnergy for JER in case of MC, don't use this scaled collection for Data
    process.scaledJetEnergyNominal = scaledJetEnergy.clone()
    process.scaledJetEnergyNominal.inputJets = "cleanPatJets"
    process.scaledJetEnergyNominal.inputMETs = "slimmedMETs"
    process.scaledJetEnergyNominal.scaleType = "jer"
    process.scaledJetEnergyNominal.resolutionEtaRanges = cms.vdouble(etaRanges)
    process.scaledJetEnergyNominal.resolutionFactors = cms.vdouble(jerSF)

    #change constraints on kineFit
    process.kinFitTtSemiLepEvent.mTop = cms.double(172.5)
    process.kinFitTtSemiLepEvent.constraints = cms.vuint32(3, 4)
    process.kinFitTtSemiLepEvent.maxNJets = cms.int32(-1)

    #object resolutions
    process.kinFitTtSemiLepEvent.udscResolutions = udscResolutionPF.functions
    process.kinFitTtSemiLepEvent.bResolutions = bjetResolutionPF.functions
    process.kinFitTtSemiLepEvent.lepResolutions = elecResolution.functions
    process.kinFitTtSemiLepEvent.metResolutions = metResolutionPF.functions
    process.kinFitTtSemiLepEvent.metResolutions[0].eta = "9999"

    process.kinFitTtSemiLepEvent.jets = cms.InputTag("cleanPatJets")
    process.kinFitTtSemiLepEvent.leps=cms.InputTag('cleanPatElectronsUser')
    process.kinFitTtSemiLepEvent.mets=cms.InputTag('slimmedMETs') # no cleanPatMET available

    if not isData :
        process.kinFitTtSemiLepEvent.jetEnergyResolutionEtaBinning = cms.vdouble(etaValues)
        process.kinFitTtSemiLepEvent.jetEnergyResolutionScaleFactors = cms.vdouble(jerSF)
        process.cleanPatJetsNominal = process.cleanPatJets.clone()
        process.cleanPatJetsNominal.src = cms.InputTag("scaledJetEnergyNominal:cleanPatJets")
        process.cleanPatJetsNominal.preselection = cms.string("pt>20 && abs(eta)<2.5")
        process.kinFitTtSemiLepEvent.jets = cms.InputTag("cleanPatJetsNominal")
        process.kinFitTtSemiLepEvent.mets = cms.InputTag("scaledJetEnergyNominal:slimmedMETs")

    #set b-tagging in KineFit
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
    process.kinFitTtSemiLepEvent.bTagAlgo = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags")
    #process.kinFitTtSemiLepEvent.minBDiscBJets= cms.double(0.5426)
    process.kinFitTtSemiLepEvent.minBDiscBJets= cms.double(0.8484)
    #process.kinFitTtSemiLepEvent.minBDiscBJets= cms.double(0.9535)
    process.kinFitTtSemiLepEvent.maxBDiscLightJets = cms.double(3.0)
    process.kinFitTtSemiLepEvent.useBTagging  = cms.bool(True)

    # Add JES Up and Down and Rerun the KineFitter
    # JESUp
    process.scaledJetEnergyUp = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyUp.inputJets = "cleanPatJets"
    process.scaledJetEnergyUp.inputMETs = "slimmedMETs"
    process.scaledJetEnergyUp.scaleType = "jes:up"
    process.cleanPatJetsJESUp = process.cleanPatJets.clone()
    process.cleanPatJetsJESUp.src = cms.InputTag("scaledJetEnergyUp:cleanPatJets")
    process.cleanPatJetsJESUp.preselection = cms.string("pt>20 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJESUp = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJESUp.jets = cms.InputTag("cleanPatJetsJESUp")
    process.kinFitTtSemiLepEventJESUp.mets = cms.InputTag("scaledJetEnergyUp:slimmedMETs")

    # JESDown
    process.scaledJetEnergyDown = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyDown.inputJets = "cleanPatJets"
    process.scaledJetEnergyDown.inputMETs = "slimmedMETs"
    process.scaledJetEnergyDown.scaleType = "jes:down"
    process.cleanPatJetsJESDown = process.cleanPatJets.clone()
    process.cleanPatJetsJESDown.src = cms.InputTag("scaledJetEnergyDown:cleanPatJets")
    process.cleanPatJetsJESDown.preselection = cms.string("pt>20 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJESDown = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJESDown.jets = cms.InputTag("cleanPatJetsJESDown")
    process.kinFitTtSemiLepEventJESDown.mets = cms.InputTag("scaledJetEnergyDown:slimmedMETs")

    # Add JER Up and Down and Rerun the KineFitter
    # JERUp
    process.scaledJetEnergyResnUp = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyResnUp.inputJets = "cleanPatJets"
    process.scaledJetEnergyResnUp.inputMETs = "slimmedMETs"
    process.scaledJetEnergyResnUp.scaleType = "jer"
    process.scaledJetEnergyResnUp.resolutionFactors = cms.vdouble(jerSFUp)
    process.cleanPatJetsResnUp = process.cleanPatJets.clone()
    process.cleanPatJetsResnUp.src = cms.InputTag("scaledJetEnergyResnUp:cleanPatJets")
    process.cleanPatJetsResnUp.preselection = cms.string("pt>20 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJERUp = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJERUp.jets = cms.InputTag("cleanPatJetsResnUp")
    process.kinFitTtSemiLepEventJERUp.mets = cms.InputTag("scaledJetEnergyResnUp:slimmedMETs")

    # JERDown
    process.scaledJetEnergyResnDown = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyResnDown.inputJets = "cleanPatJets"
    process.scaledJetEnergyResnDown.inputMETs = "slimmedMETs"
    process.scaledJetEnergyResnDown.scaleType = "jer"
    process.scaledJetEnergyResnDown.resolutionFactors = cms.vdouble(jerSFDown)
    process.cleanPatJetsResnDown = process.cleanPatJets.clone()
    process.cleanPatJetsResnDown.src = cms.InputTag("scaledJetEnergyResnDown:cleanPatJets")
    process.cleanPatJetsResnDown.preselection = cms.string("pt>20 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJERDown = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJERDown.jets = cms.InputTag("cleanPatJetsResnDown")
    process.kinFitTtSemiLepEventJERDown.mets = cms.InputTag("scaledJetEnergyResnDown:slimmedMETs")

    #Put them in a sequence
    if isData:
        process.kinFitSequence = cms.Sequence(process.cleanPatMuons*
                process.cleanPatElectronsUser*
                process.cleanPatPhotons*
                process.cleanPatTaus*
                process.cleanPatJets*
                process.kinFitTtSemiLepEvent)
    if not isData:
        process.kinFitSequence = cms.Sequence(process.cleanPatMuons*
                process.cleanPatElectronsUser*
                process.cleanPatPhotons*
                process.cleanPatTaus*
                process.cleanPatJets*
                process.scaledJetEnergyNominal *
                process.cleanPatJetsNominal *
                process.kinFitTtSemiLepEvent*
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
                process.kinFitTtSemiLepEventJERDown
                )
    toPrint("jets used in Kinematic fit", process.kinFitTtSemiLepEvent.jets)

