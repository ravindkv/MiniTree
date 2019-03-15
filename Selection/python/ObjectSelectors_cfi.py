import FWCore.ParameterSet.Config as cms

#my base values for trigger bit selection -------------------
BaseTriggerSet = cms.PSet( source = cms.InputTag("TriggerResults::HLT"),
                           trigBits = cms.vstring('HLT_IsoMu24'),
                           sourceFilter = cms.InputTag("TriggerResults"),
                           metFilterBits = cms.vstring('Flag_goodVertices')
                           )

#my base values for vertex selection ---------------------------------
BaseVertexSet = cms.PSet( vertexSource = cms.InputTag("offlineSlimmedPrimaryVertices"),
                          maxZ = cms.double(24),
                          rho =  cms.InputTag('fixedGridRhoFastjetAll'),
                          maxRho = cms.double(2.0),
                          minNDOF = cms.int32(4)
                          )

#my base values for muon selection ---------------------------------------
BaseMuonsSet =  cms.PSet( sources = cms.InputTag("slimmedMuons"),
                          minPt = cms.double(10),
                          maxEta = cms.double(3.0)
                          )

# base values for electron selection ------------------------------------
BaseElectronsSet =  cms.PSet(sources = cms.InputTag("slimmedElectrons"),
                        minEt = cms.double(10),
                        maxEta = cms.double(3.0),
                        rhoIso = cms.InputTag("fixedGridRhoFastjetAll"),
                        conversionsMiniAOD  = cms.InputTag('reducedEgamma:reducedConversions'),
                        beamSpot = cms.InputTag('offlineBeamSpot')
                        )

#my base values for jet selection -----------------------------------------------
BaseJetsSet = cms.PSet(sources = cms.InputTag("updatedPatJetsUpdatedJEC"),
                       #sources = cms.InputTag("slimmedJets"),
                       minPt = cms.double(17),
                       maxEta = cms.double(4.0),
                       jet_rho = cms.InputTag('fixedGridRhoFastjetAll'),
                       resolutionsFile = cms.string("Summer16_25nsV1_MC_PtResolution_AK4PF.txt"),
                       scaleFactorsFile= cms.string("Summer16_25nsV1_MC_SF_AK4PF.txt")
                       )

#my base values for met selection ------------------------------------------------
BaseMetsSet = cms.PSet(sources = cms.InputTag("slimmedMETs"),
                       minMET = cms.double(10)
                       )

#my MC truth matching sets -------------------------------------------------------
BaseMCTruthSet = cms.PSet(sampleCode = cms.string("ttbar"),
                       sampleChannel = cms.string("electron")
                       )

# set of collections from KinFit -------------------------------------------------------
# The process.kinFitSequence is run on fly. The process.myMiniTreeProducer is run
#after that to store kinfit objects in the ntuple
kinFitTagsFromProducer = []
kinFitTagsFromProducer.append("kinFitTtSemiLepEvent:Leptons")
kinFitTagsFromProducer.append("kinFitTtSemiLepEvent:Neutrinos")
kinFitTagsFromProducer.append("kinFitTtSemiLepEvent:PartonsHadB")
kinFitTagsFromProducer.append("kinFitTtSemiLepEvent:PartonsHadP")
kinFitTagsFromProducer.append("kinFitTtSemiLepEvent:PartonsHadQ")
kinFitTagsFromProducer.append("kinFitTtSemiLepEvent:PartonsLepB")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESUp:Leptons")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESUp:Neutrinos")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESUp:PartonsHadB")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESUp:PartonsHadP")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESUp:PartonsHadQ")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESUp:PartonsLepB")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESDown:Leptons")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESDown:Neutrinos")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESDown:PartonsHadB")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESDown:PartonsHadP")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESDown:PartonsHadQ")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJESDown:PartonsLepB")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERUp:Leptons")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERUp:Neutrinos")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERUp:PartonsHadB")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERUp:PartonsHadP")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERUp:PartonsHadQ")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERUp:PartonsLepB")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERDown:Leptons")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERDown:Neutrinos")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERDown:PartonsHadB")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERDown:PartonsHadP")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERDown:PartonsHadQ")
kinFitTagsFromProducer.append("kinFitTtSemiLepEventJERDown:PartonsLepB")

BaseKFPSet = cms.PSet(sources = cms.VInputTag(kinFitTagsFromProducer),
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
