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

