import FWCore.ParameterSet.Config as cms

#my base values for trigger bit selection -------------------
BaseTriggerSet = cms.PSet( source = cms.InputTag("TriggerResults::HLT"),
                           #bits = cms.vstring('HLT_Mu9','HLT_Ele10_LW_L1R_v2','HLT_Jet30'),
                           bits = cms.vstring('HLT_AK4CaloJet30_v3','HLT_HcalPhiSym_v2','HLT_HcalPhiSym_v2'),
                           )

#my base values for vertex selection ---------------------------------
BaseVertexSet = cms.PSet( vertexSource = cms.InputTag("offlineSlimmedPrimaryVertices"),
                          maxZ = cms.double(24),
                          maxRho = cms.double(2.0),
                          minNDOF = cms.int32(4),
                          beamSpotSource = cms.InputTag("offlineBeamSpot"),
                          useBeamSpot = cms.bool(True)
                          )

#my base values for tracks selection ----------------------------------
BaseTrackSet = cms.PSet( source = cms.InputTag("generalTracks"),
                         dedxSource = cms.InputTag("dedxHarmonic2"),
                         minPt = cms.double(1),
                         maxEta = cms.double(2.5),
                         minQuality = cms.int32(2),
                         maxD0 = cms.double(400),
                         maxTrackChi2 = cms.double(10),
                         minTrackValidHits = cms.int32(5),
                         minPixelHits = cms.int32(1),
                         minPrimaryVertexWeight = cms.double(0),
                         minDeltaRtoLepton = cms.double(0.1),
                         trackIsoCone = cms.double(0.3),
                         maxPtSumInTrackIsoCone = cms.double(10)
                         )



#my base values for muon selection ---------------------------------------
BaseMuonsSet =  cms.PSet( sources = cms.InputTag("slimmedMuons"),
                          #triggerEvent = cms.InputTag("patTriggerEvent"),
                          triggerEvent = cms.InputTag("patTrigger"),
                          triggerMatch = cms.string("TrigMatch"),

                          minPt = cms.double(10),
                          maxEta = cms.double(2.4),
                          minMuonHits = cms.int32(0),
                          minMatchStations = cms.int32(1),
                          minPixelHits = cms.int32(0),
                          minTrackerLayers = cms.int32(5),
                          maxRelIso = cms.double(0.25),
                          )



# base values for electron selection ----------------------------------------------
BaseElectronsSet =  cms.PSet(sources = cms.InputTag("slimmedElectrons"),
                        dedxSource = cms.InputTag("dedxHarmonic2"),
                        #triggerEvent = cms.InputTag("patTriggerEvent"),
                        triggerEvent = cms.InputTag("patTrigger"),
                        triggerMatch = cms.string("TrigMatch"),

                        id = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-loose'),
                        #id = cms.string('cutBasedElectronID-Summer16-80X-V1-loose'),
                        maxRelCombPFIsoEA = cms.double(0.0994),
                        minEt = cms.double(10),
                        maxEta = cms.double(2.5),
                        mvacut = cms.double(0.30),
                        #rho = cms.InputTag("kt6PFJets", "rho")
#https://github.com/ikrav/cmssw/blob/egm_id_80X_v1/RecoEgamma/ElectronIdentification/python/Identification/cutBasedElectronID_tools.py#L317
                        rhoIso = cms.InputTag("fixedGridRhoFastjetAll")
                        )

#my base values for jet selection -----------------------------------------------
BaseJetsSet = cms.PSet(sources = cms.InputTag("slimmedJets"),
                       CaloJetId = cms.PSet( version = cms.string("PURE09"), quality = cms.string("LOOSE") ),
                       PFJetId = cms.PSet( version = cms.string("FIRSTDATA"), quality = cms.string("LOOSE") ),
                       dedxSource = cms.InputTag("dedxHarmonic2"),
                       #triggerEvent = cms.InputTag("patTriggerEvent"),
                       triggerEvent = cms.InputTag("hltTriggerSummaryAOD"),
                       #triggerEvent = cms.InputTag("selectedPatTrigger"),
                       triggerMatch = cms.string("TrigMatch"),
                       useRawJets = cms.bool(False),
                       minPt = cms.double(17),
                       maxEta = cms.double(2.5),
                       minDeltaRtoLepton = cms.double(0.4),
                       puMVADiscriminant = cms.InputTag("puJetMva:fullDiscriminant"),
                       puMVAID = cms.InputTag("puJetMva:fullId"),
                       puMVADiscriminantResCor = cms.InputTag("puJetMvaResCor:fullDiscriminant"),
                       puMVAIDResCor = cms.InputTag("puJetMvaResCor:fullId")
                       )

#my base values for met selection ------------------------------------------------
BaseMetsSet = cms.PSet(sources = cms.InputTag("slimmedMETs"),
                       minMET = cms.double(10)
                       )

#my MC truth matching sets -------------------------------------------------------
BaseMCTruthSet = cms.PSet( isData = cms.bool(False),
                       producePDFweights = cms.bool(False),
                       sampleCode = cms.string("SEECODES"),
                       sampleChannel = cms.string("electron"),
                       jpMatchSources = cms.VInputTag("selectedPatJetsByRef", "selectedPatJetsAK5JPTByRef", "selectedPatJetsAK5PFByRef", "selectedPatJetsPFlowByRef")
                       )

BaseKFPSet = cms.PSet(sources = cms.VInputTag("kinFitTtSemiLepEvent:Leptons","kinFitTtSemiLepEvent:Neutrinos","kinFitTtSemiLepEvent:PartonsHadB","kinFitTtSemiLepEvent:PartonsHadP","kinFitTtSemiLepEvent:PartonsHadQ","kinFitTtSemiLepEvent:PartonsLepB","kinFitTtSemiLepEventJESUp:Leptons","kinFitTtSemiLepEventJESUp:Neutrinos","kinFitTtSemiLepEventJESUp:PartonsHadB","kinFitTtSemiLepEventJESUp:PartonsHadP","kinFitTtSemiLepEventJESUp:PartonsHadQ","kinFitTtSemiLepEventJESUp:PartonsLepB","kinFitTtSemiLepEventJESDown:Leptons","kinFitTtSemiLepEventJESDown:Neutrinos","kinFitTtSemiLepEventJESDown:PartonsHadB","kinFitTtSemiLepEventJESDown:PartonsHadP","kinFitTtSemiLepEventJESDown:PartonsHadQ","kinFitTtSemiLepEventJESDown:PartonsLepB","kinFitTtSemiLepEventJERUp:Leptons","kinFitTtSemiLepEventJERUp:Neutrinos","kinFitTtSemiLepEventJERUp:PartonsHadB","kinFitTtSemiLepEventJERUp:PartonsHadP","kinFitTtSemiLepEventJERUp:PartonsHadQ","kinFitTtSemiLepEventJERUp:PartonsLepB","kinFitTtSemiLepEventJERDown:Leptons","kinFitTtSemiLepEventJERDown:Neutrinos","kinFitTtSemiLepEventJERDown:PartonsHadB","kinFitTtSemiLepEventJERDown:PartonsHadP","kinFitTtSemiLepEventJERDown:PartonsHadQ","kinFitTtSemiLepEventJERDown:PartonsLepB"),
                      njetsUsed = cms.InputTag("kinFitTtSemiLepEvent:NumberOfConsideredJets"),
                      chi2OfFit = cms.InputTag("kinFitTtSemiLepEvent:Chi2"),
                      probOfFit = cms.InputTag("kinFitTtSemiLepEvent:Prob"),
                      statusOfFit = cms.InputTag("kinFitTtSemiLepEvent:Status"),
                      njetsUsedUp = cms.InputTag("kinFitTtSemiLepEventJESUp:NumberOfConsideredJets"),
                      chi2OfFitUp = cms.InputTag("kinFitTtSemiLepEventJESUp:Chi2"),
                      probOfFitUp = cms.InputTag("kinFitTtSemiLepEventJESUp:Prob"),
                      statusOfFitUp = cms.InputTag("kinFitTtSemiLepEventJESUp:Status"),
                      njetsUsedDown = cms.InputTag("kinFitTtSemiLepEventJESDown:NumberOfConsideredJets"),
                      chi2OfFitDown = cms.InputTag("kinFitTtSemiLepEventJESDown:Chi2"),
                      probOfFitDown = cms.InputTag("kinFitTtSemiLepEventJESDown:Prob"),
                      statusOfFitDown = cms.InputTag("kinFitTtSemiLepEventJESDown:Status"),
                      njetsUsedJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp:NumberOfConsideredJets"),
                      chi2OfFitJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp:Chi2"),
                      probOfFitJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp:Prob"),
                      statusOfFitJERUp = cms.InputTag("kinFitTtSemiLepEventJERUp:Status"),
                      njetsUsedJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown:NumberOfConsideredJets"),
                      chi2OfFitJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown:Chi2"),
                      probOfFitJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown:Prob"),
                      statusOfFitJERDown = cms.InputTag("kinFitTtSemiLepEventJERDown:Status"),
                      runKineFitter = cms.bool(False)
                      )
