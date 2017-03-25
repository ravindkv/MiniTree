import FWCore.ParameterSet.Config as cms

from TopQuarkAnalysis.TopObjectResolutions.stringResolutions_etEtaPhi_Fall11_cff import *
from MiniTree.Utilities.JetEnergyScale_cfi import *
from MiniTree.Selection.LocalSources_cff import toPrint

def addSemiLepKinFitMuon(process, isData=False) :

    ## std sequence to produce the kinematic fit for semi-leptonic events
    process.load("TopQuarkAnalysis.TopKinFitter.TtSemiLepKinFitProducer_Muons_cfi")
    process.load( "PhysicsTools.PatAlgos.patSequences_cff" )

    #apply selections on muon
    process.selectedPatMuons.src = cms.InputTag("slimmedMuons")
    process.cleanPatMuons.preselection = cms.string("pt>25 && abs(eta)<2.1"+
                                                    " && isGlobalMuon && isPFMuon && isTrackerMuon" +
                                                    " && globalTrack.isNonnull "+
                                                    " && globalTrack.normalizedChi2<10"+
                                                    " && globalTrack.hitPattern.numberOfValidMuonHits>0"+
                                                    " && numberOfMatchedStations>1"+
                                                    " && innerTrack.hitPattern.numberOfValidPixelHits>0"+
                                                    " && track.hitPattern.trackerLayersWithMeasurement > 5"+
                                                    " && dB() < 0.2"+
                                                    " && (pfIsolationR04.sumChargedHadronPt+ max(0.,pfIsolationR04.sumNeutralHadronEt+pfIsolationR04.sumPhotonEt-0.5*pfIsolationR04.sumPUPt))/pt < 0.30")
    #these inputs are required for cleanPatJets
    process.selectedPatElectrons.src = cms.InputTag("slimmedElectrons")
    process.selectedPatPhotons.src = cms.InputTag("slimmedPhotons")
    process.selectedPatTaus.src = cms.InputTag("slimmedTaus")

    #clean jets from muons
    process.selectedPatJets.src = cms.InputTag("slimmedJets")
    process.cleanPatJets.preselection = cms.string("pt>20 && abs(eta)<2.5")
    process.cleanPatJets.checkOverlaps.muons.requireNoOverlaps  = cms.bool(True)

    #clean taus
    '''
    process.cleanPatTaus.preselection = cms.string('tauID("decayModeFinding") > 0.5 &'
            'tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") > 0.5 &'
            ' tauID("againstMuonTight3") > 0.5 &'
            ' tauID("againstElectronVLooseMVA5") > 0.5'
            )
    '''
    #only used for data
    process.cleanPatJetsResCor = process.cleanPatJets.clone()
    ##process.cleanPatJetsResCor.src = cms.InputTag("selectedPatJetsResCor")
    process.cleanPatJetsResCor.preselection = cms.string("pt>24 && abs(eta)<2.5")

    #smear the JetEnergy for JER in case of MC, don't use this scaled collection for Data
    process.scaledJetEnergyNominal = scaledJetEnergy.clone()
    process.scaledJetEnergyNominal.inputJets = "slimmedJets"
    process.scaledJetEnergyNominal.inputMETs = "slimmedMETs"
    process.scaledJetEnergyNominal.scaleType = "jer"
    process.scaledJetEnergyNominal.resolutionEtaRanges = cms.vdouble(
        0.0, 0.5, 0.5, 1.1, 1.1, 1.7, 1.7, 2.3, 2.3, -1.0 )
    process.scaledJetEnergyNominal.resolutionFactors = cms.vdouble(
        1.052, 1.057, 1.096, 1.134, 1.288 )

    #change constraints on kineFit
    process.kinFitTtSemiLepEvent.mTop = cms.double(172.5)
    process.kinFitTtSemiLepEvent.constraints = cms.vuint32(3, 4)
    process.kinFitTtSemiLepEvent.maxNJets = cms.int32(-1)
    process.kinFitTtSemiLepEvent.udscResolutions = udscResolutionPF.functions
    process.kinFitTtSemiLepEvent.bResolutions = bjetResolutionPF.functions
    process.kinFitTtSemiLepEvent.lepResolutions = muonResolution.functions
    process.kinFitTtSemiLepEvent.metResolutions = metResolutionPF.functions
    process.kinFitTtSemiLepEvent.metResolutions[0].eta = "9999"

    process.kinFitTtSemiLepEvent.jets=cms.InputTag('slimmedJets')
    if isData:
        process.kinFitTtSemiLepEvent.jets = cms.InputTag("cleanPatJetsResCor")
    process.kinFitTtSemiLepEvent.leps=cms.InputTag('slimmedMuons')
    process.kinFitTtSemiLepEvent.mets=cms.InputTag('slimmedMETs')

    if not isData :
        process.kinFitTtSemiLepEvent.jetEnergyResolutionScaleFactors = cms.vdouble (
            1.052, 1.057, 1.096, 1.134, 1.288  )
        process.kinFitTtSemiLepEvent.jetEnergyResolutionEtaBinning = cms.vdouble(
            0.0, 0.5, 1.1, 1.7, 2.3, -1. )
        process.cleanPatJetsNominal = process.cleanPatJets.clone()
        process.cleanPatJetsNominal.src = cms.InputTag("scaledJetEnergyNominal:slimmedJets")
        process.cleanPatJetsNominal.preselection = cms.string("pt>24 && abs(eta)<2.5")
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
    process.scaledJetEnergyUp.inputJets = "slimmedJets"
    process.scaledJetEnergyUp.inputMETs = "slimmedMETs"
    process.scaledJetEnergyUp.scaleType = "jes:up"
    process.cleanPatJetsJESUp = process.cleanPatJets.clone()
    process.cleanPatJetsJESUp.src = cms.InputTag("scaledJetEnergyUp:slimmedJets")
    process.cleanPatJetsJESUp.preselection = cms.string("pt>24 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJESUp = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJESUp.jets = cms.InputTag("cleanPatJetsJESUp")
    process.kinFitTtSemiLepEventJESUp.mets = cms.InputTag("scaledJetEnergyUp:slimmedMETs")

    # JESDown
    process.scaledJetEnergyDown = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyDown.inputJets = "slimmedJets"
    process.scaledJetEnergyDown.inputMETs = "slimmedMETs"
    process.scaledJetEnergyDown.scaleType = "jes:down"
    process.cleanPatJetsJESDown = process.cleanPatJets.clone()
    process.cleanPatJetsJESDown.src = cms.InputTag("scaledJetEnergyDown:slimmedJets")
    process.cleanPatJetsJESDown.preselection = cms.string("pt>24 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJESDown = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJESDown.jets = cms.InputTag("cleanPatJetsJESDown")
    process.kinFitTtSemiLepEventJESDown.mets = cms.InputTag("scaledJetEnergyDown:slimmedMETs")

    # Add JER Up and Down and Rerun the KineFitter
    # JERUp
    process.scaledJetEnergyResnUp = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyResnUp.inputJets = "slimmedJets"
    process.scaledJetEnergyResnUp.inputMETs = "slimmedMETs"
    process.scaledJetEnergyResnUp.scaleType = "jer"
    process.scaledJetEnergyResnUp.resolutionFactors = cms.vdouble(
        1.115, 1.114, 1.161, 1.228, 1.488 )
    process.cleanPatJetsResnUp = process.cleanPatJets.clone()
    process.cleanPatJetsResnUp.src = cms.InputTag("scaledJetEnergyResnUp:slimmedJets")
    process.cleanPatJetsResnUp.preselection = cms.string("pt>24 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJERUp = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJERUp.jets = cms.InputTag("cleanPatJetsResnUp")
    process.kinFitTtSemiLepEventJERUp.mets = cms.InputTag("scaledJetEnergyResnUp:slimmedMETs")

    # JERDown
    process.scaledJetEnergyResnDown = process.scaledJetEnergyNominal.clone()
    process.scaledJetEnergyResnDown.inputJets = "slimmedJets"
    process.scaledJetEnergyResnDown.inputMETs = "slimmedMETs"
    process.scaledJetEnergyResnDown.scaleType = "jer"
    process.scaledJetEnergyResnDown.resolutionFactors = cms.vdouble(
        0.990, 1.001, 1.032, 1.042, 1.089 )
    process.cleanPatJetsResnDown = process.cleanPatJets.clone()
    process.cleanPatJetsResnDown.src = cms.InputTag("scaledJetEnergyResnDown:slimmedJets")
    process.cleanPatJetsResnDown.preselection = cms.string("pt>24 && abs(eta)<2.5")
    process.kinFitTtSemiLepEventJERDown = process.kinFitTtSemiLepEvent.clone()
    process.kinFitTtSemiLepEventJERDown.jets = cms.InputTag("cleanPatJetsResnDown")
    process.kinFitTtSemiLepEventJERDown.mets = cms.InputTag("scaledJetEnergyResnDown:slimmedMETs")

    process.kinFitSequence = cms.Sequence(process.cleanPatJetsResCor* process.kinFitTtSemiLepEvent)
    if isData :
        process.kinFitSequence.remove(process.cleanPatJetsResCor)
        process.kinFitSequence.replace(process.kinFitTtSemiLepEvent,
                process.scaledJetEnergyNominal*process.selectedPatMuons*
                process.selectedPatElectrons* process.selectedPatPhotons*
                process.selectedPatTaus* process.selectedPatJets*
                process.cleanPatMuons* process.cleanPatElectrons*
                process.cleanPatPhotons*process.cleanPatTaus*
                process.cleanPatJets*process.cleanPatJetsResCor* process.kinFitTtSemiLepEvent)

    if not isData :
        process.kinFitSequence.remove(process.cleanPatJetsResCor)
        process.kinFitSequence.replace(process.kinFitTtSemiLepEvent,
                process.scaledJetEnergyNominal* process.selectedPatMuons*
                process.selectedPatElectrons* process.selectedPatPhotons*
                process.selectedPatTaus* process.selectedPatJets*
                process.cleanPatMuons* process.cleanPatElectrons*
                process.cleanPatPhotons*process.cleanPatTaus*
                process.cleanPatJets* process.cleanPatJetsNominal*
                process.kinFitTtSemiLepEvent* process.scaledJetEnergyUp*
                process.cleanPatJetsJESUp* process.kinFitTtSemiLepEventJESUp*
                process.scaledJetEnergyDown* process.cleanPatJetsJESDown*
                process.kinFitTtSemiLepEventJESDown* process.scaledJetEnergyResnUp*
                process.cleanPatJetsResnUp* process.kinFitTtSemiLepEventJERUp*
                process.scaledJetEnergyResnDown* process.cleanPatJetsResnDown*
                process.kinFitTtSemiLepEventJERDown)

    #print "// jet input to cleanPatJetsResCor:", process.cleanPatJetsResCor.src," //"
    toPrint("jets used in Kinematic fit", process.kinFitTtSemiLepEvent.jets)

