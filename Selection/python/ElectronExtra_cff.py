import FWCore.ParameterSet.Config as cms
import copy
from CommonTools.ParticleFlow.pfParticleSelection_cff import *
#https://github.com/cms-sw/cmssw/blob/CMSSW_9_2_6_patchX/RecoEgamma/ElectronIdentification/python/Identification/cutBasedElectronID_Summer16_80X_V1_cff.py
#from RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff *

#-----------------------------
#for cut based electron ids
#-----------------------------
def configureElectronCutIdIso(process) :
    #vertex
    process.selectedPrimaryVertices = cms.EDFilter(
        "VertexSelector",
        src = cms.InputTag('offlineSlimmedPrimaryVertices'),
        cut = cms.string("isValid & ndof >= 4 & z > -24 & z < +24 & position.Rho < 2."),
        filter = cms.bool(False)
        )

    #embed electrons
    process.selectedPatElectronsUserEmbedded = cms.EDProducer(
        "ElectronsUserEmbedded",
        electronTag = cms.InputTag("slimmedElectrons"),
        vertexTag   = cms.InputTag("selectedPrimaryVertices"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        #rho = cms.InputTag("kt6PFJets", "rho"),
        beamSpot = cms.InputTag('offlineBeamSpot'),
        conversionsMiniAOD  = cms.InputTag('reducedEgamma:reducedConversions'),
        #eleIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-veto"),
        #eleIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-loose"),
        eleIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-medium")
        #eleIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-tight"),
        )
    process.EleEmbedSequence = cms.Sequence(process.selectedPrimaryVertices * process.selectedPatElectronsUserEmbedded)


'''
#-----------------------------
#for MVA electron ids
#-----------------------------
def configureElectronMVAIdIso(process) :
    process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
    process.mvaID = cms.Sequence(  process.mvaTrigV0 + process.mvaTrigNoIPV0 + process.mvaNonTrigV0 )

    #Electron ID
    process.patElectrons.electronIDSources = cms.PSet(
        #MVA
        mvaTrigV0 = cms.InputTag("mvaTrigV0"),
        mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0"),
        mvaTrigNoIPV0 = cms.InputTag("mvaTrigNoIPV0"),
        )

    from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso
    process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons')
    from CommonTools.ParticleFlow.pfParticleSelection_cff import pfParticleSelectionSequence
    process.pfParticleSelectionSequence = pfParticleSelectionSequence
    process.pfIsolationSequence = cms.Sequence(
        process.pfParticleSelectionSequence*
        process.eleIsoSequence
        )

    #Custom cone size for Electron isolation
    process.elPFIsoValueChargedAll04PFIdPFIso.deposits[0].vetos = cms.vstring(
        'EcalEndcaps:ConeVeto(0.015)'
        )
    process.elPFIsoValueCharged04PFIdPFIso.deposits[0].vetos = cms.vstring(
        'EcalEndcaps:ConeVeto(0.015)'
        )
    process.elPFIsoValueGamma04PFIdPFIso.deposits[0].vetos = cms.vstring(
        'EcalEndcaps:ConeVeto(0.08)'
        )
    process.elPFIsoValuePU04PFIdPFIso.deposits[0].vetos = cms.vstring(
        'EcalEndcaps:ConeVeto(0.015)'
        )
    process.elPFIsoValueNeutral04PFIdPFIso.deposits[0].vetos = cms.vstring()

    process.elPFIsoValueChargedAll04NoPFIdPFIso.deposits[0].vetos = cms.vstring(
        'EcalEndcaps:ConeVeto(0.015)'
        )
    process.elPFIsoValueCharged04NoPFIdPFIso.deposits[0].vetos = cms.vstring(
        'EcalEndcaps:ConeVeto(0.015)'
        )
    process.elPFIsoValueGamma04NoPFIdPFIso.deposits[0].vetos = cms.vstring(
        'EcalEndcaps:ConeVeto(0.08)'
        )
    process.elPFIsoValuePU04NoPFIdPFIso.deposits[0].vetos = cms.vstring(
        'EcalEndcaps:ConeVeto(0.015)'
        )
    process.elPFIsoValueNeutral04PFIdPFIso.deposits[0].vetos = cms.vstring()

    #Set isolation to the patElectrons
    process.patElectrons.isoDeposits = cms.PSet(
        pfAllParticles   = cms.InputTag("elPFIsoDepositPUPFIso"),      # all PU   CH+MU+E
        pfChargedHadrons = cms.InputTag("elPFIsoDepositChargedPFIso"), # all noPU CH
        pfNeutralHadrons = cms.InputTag("elPFIsoDepositNeutralPFIso"), # all NH
        pfPhotons        = cms.InputTag("elPFIsoDepositGammaPFIso"),   # all PH
        user = cms.VInputTag(
         cms.InputTag("elPFIsoDepositChargedAllPFIso"),                 # all noPU CH+MU+E
         )
        )
    process.patElectrons.isolationValues = cms.PSet(
        pfAllParticles   = cms.InputTag("elPFIsoValuePU04PFIdPFIso"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04PFIdPFIso"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04PFIdPFIso"),
        pfPhotons        = cms.InputTag("elPFIsoValueGamma04PFIdPFIso"),
        user = cms.VInputTag(
         cms.InputTag("elPFIsoValueChargedAll04PFIdPFIso"),
         )
        )
    process.patElectrons.isolationValuesNoPFId = cms.PSet(
        pfAllParticles   = cms.InputTag("elPFIsoValuePU04NoPFIdPFIso"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04NoPFIdPFIso"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04NoPFIdPFIso"),
        pfPhotons        = cms.InputTag("elPFIsoValueGamma04NoPFIdPFIso"),
        user = cms.VInputTag(
         cms.InputTag("elPFIsoValueChargedAll04NoPFIdPFIso")
         )
        )

    ################### vertex sequence ####################

    process.selectedPrimaryVertices = cms.EDFilter(
        "VertexSelector",
        src = cms.InputTag('offlineSlimmedPrimaryVertices'),
        cut = cms.string("isValid & ndof >= 4 & z > -24 & z < +24 & position.Rho < 2."),
        filter = cms.bool(False)
        )

    #process.primaryVertexCounter = cms.EDFilter(
    #    "VertexCountFilter",
    #    src = cms.InputTag('selectedPrimaryVertices'),
    #    minNumber = cms.uint32(1),
    #    maxNumber = cms.uint32(999),
    #    )
    ########Embed elctrons with variable to cut on############
    process.selectedPatElectronsUserEmbedded = cms.EDProducer(
        "ElectronsUserEmbedded",
        electronTag = cms.InputTag("slimmedElectrons"),
        vertexTag   = cms.InputTag("selectedPrimaryVertices"),
        rho = cms.InputTag("fixedGridRhoFastjetAll")
        #rho = cms.InputTag("kt6PFJets", "rho")
        )
    process.EleEmbedSequence = cms.Sequence(process.selectedPrimaryVertices * process.selectedPatElectronsUserEmbedded)
'''
