*** Including object resolutions derived from Fall11 MC for:
*** - electrons   - muons   - udscJetsPF     - bJetsPF     - pfMET
*** Please make sure that you are really using resolutions that are suited for the objects in your analysis!
# Conditions read from  CMS_CONDITIONS  via FrontierProd 
10-Feb-2017 08:21:13 CET  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/RunIISpring16MiniAODv1/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FED53EE4-7D16-E611-AE17-B083FED406AD.root
10-Feb-2017 08:21:17 CET  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/RunIISpring16MiniAODv1/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FED53EE4-7D16-E611-AE17-B083FED406AD.root
Begin processing the 1st record. Run 1, Event 26354, LumiSection 37 at 10-Feb-2017 08:22:05.975 CET
----- Begin Fatal Exception 10-Feb-2017 08:22:06 CET-----------------------
An exception of category 'ProductNotFound' occurred while
   [0] Processing run: 1 lumi: 37 event: 26354
   [1] Running path 'outpath'
   [2] Calling event method for module PoolOutputModule/'out'
   [3] Calling produce method for unscheduled module PATJetProducer/'patJets'
   [4] Calling produce method for unscheduled module JetFlavourClustering/'patJetFlavourAssociation'
   [5] Calling produce method for unscheduled module HadronAndPartonSelector/'patJetPartons'
Exception Message:
Principal::getByToken: Found zero products matching all criteria
Looking for type: std::vector<reco::GenParticle>
Looking for module label: genParticles
Looking for productInstanceName: 

   Additional Info:
      [a] If you wish to continue processing events after a ProductNotFound exception,
add "SkipEvent = cms.untracked.vstring('ProductNotFound')" to the "options" PSet in the configuration.

----- End Fatal Exception -------------------------------------------------
10-Feb-2017 08:22:06 CET  Closed file root://eoscms.cern.ch//eos/cms/store/mc/RunIISpring16MiniAODv1/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FED53EE4-7D16-E611-AE17-B083FED406AD.root

TrigReport ---------- Event  Summary ------------
TrigReport Events total = 1 passed = 1 failed = 0

TrigReport ---------- Path   Summary ------------
TrigReport  Trig Bit#   Executed     Passed     Failed      Error Name

TrigReport -------End-Path   Summary ------------
TrigReport  Trig Bit#   Executed     Passed     Failed      Error Name
TrigReport     0    0          1          0          0          1 outpath

TrigReport ------ Modules in End-Path: outpath ------------
TrigReport  Trig Bit#    Visited     Passed     Failed      Error Name
TrigReport     0    0          1          0          0          1 out

TrigReport ---------- Module Summary ------------
TrigReport    Visited   Executed     Passed     Failed      Error Name
TrigReport          0          0          0          0          0 ak4CaloL1FastL2L3Corrector
TrigReport          0          0          0          0          0 ak4CaloL1FastL2L3L6Corrector
TrigReport          0          0          0          0          0 ak4CaloL1FastL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4CaloL1FastjetCorrector
TrigReport          0          0          0          0          0 ak4CaloL1L2L3Corrector
TrigReport          0          0          0          0          0 ak4CaloL1L2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4CaloL1OffsetCorrector
TrigReport          0          0          0          0          0 ak4CaloL2L3Corrector
TrigReport          0          0          0          0          0 ak4CaloL2L3L6Corrector
TrigReport          0          0          0          0          0 ak4CaloL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4CaloL2RelativeCorrector
TrigReport          0          0          0          0          0 ak4CaloL3AbsoluteCorrector
TrigReport          0          0          0          0          0 ak4CaloL6SLBCorrector
TrigReport          0          0          0          0          0 ak4CaloResidualCorrector
TrigReport          0          0          0          0          0 ak4JPTL1FastL2L3Corrector
TrigReport          0          0          0          0          0 ak4JPTL1FastL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4JPTL1FastjetCorrector
TrigReport          0          0          0          0          0 ak4JPTL1L2L3Corrector
TrigReport          0          0          0          0          0 ak4JPTL1L2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4JPTL1OffsetCorrector
TrigReport          0          0          0          0          0 ak4JPTL2L3Corrector
TrigReport          0          0          0          0          0 ak4JPTL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4JPTL2RelativeCorrector
TrigReport          0          0          0          0          0 ak4JPTL3AbsoluteCorrector
TrigReport          0          0          0          0          0 ak4JPTResidualCorrector
TrigReport          0          0          0          0          0 ak4L1JPTOffsetCorrector
TrigReport          0          0          0          0          0 ak4PFCHSL1FastL2L3Corrector
TrigReport          0          0          0          0          0 ak4PFCHSL1FastL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4PFCHSL1FastjetCorrector
TrigReport          0          0          0          0          0 ak4PFCHSL1L2L3Corrector
TrigReport          0          0          0          0          0 ak4PFCHSL1L2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4PFCHSL1OffsetCorrector
TrigReport          0          0          0          0          0 ak4PFCHSL2L3Corrector
TrigReport          0          0          0          0          0 ak4PFCHSL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4PFCHSL2RelativeCorrector
TrigReport          0          0          0          0          0 ak4PFCHSL3AbsoluteCorrector
TrigReport          0          0          0          0          0 ak4PFCHSResidualCorrector
TrigReport          0          0          0          0          0 ak4PFL1FastL2L3Corrector
TrigReport          0          0          0          0          0 ak4PFL1FastL2L3L6Corrector
TrigReport          0          0          0          0          0 ak4PFL1FastL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4PFL1FastjetCorrector
TrigReport          0          0          0          0          0 ak4PFL1L2L3Corrector
TrigReport          0          0          0          0          0 ak4PFL1L2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4PFL1OffsetCorrector
TrigReport          0          0          0          0          0 ak4PFL2L3Corrector
TrigReport          0          0          0          0          0 ak4PFL2L3L6Corrector
TrigReport          0          0          0          0          0 ak4PFL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4PFL2RelativeCorrector
TrigReport          0          0          0          0          0 ak4PFL3AbsoluteCorrector
TrigReport          0          0          0          0          0 ak4PFL6SLBCorrector
TrigReport          0          0          0          0          0 ak4PFPuppiL1FastL2L3Corrector
TrigReport          0          0          0          0          0 ak4PFPuppiL1FastL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4PFPuppiL1FastjetCorrector
TrigReport          0          0          0          0          0 ak4PFPuppiL1L2L3Corrector
TrigReport          0          0          0          0          0 ak4PFPuppiL1L2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4PFPuppiL1OffsetCorrector
TrigReport          0          0          0          0          0 ak4PFPuppiL2L3Corrector
TrigReport          0          0          0          0          0 ak4PFPuppiL2L3ResidualCorrector
TrigReport          0          0          0          0          0 ak4PFPuppiL2RelativeCorrector
TrigReport          0          0          0          0          0 ak4PFPuppiL3AbsoluteCorrector
TrigReport          0          0          0          0          0 ak4PFPuppiResidualCorrector
TrigReport          0          0          0          0          0 ak4PFResidualCorrector
TrigReport          0          0          0          0          0 ak4TrackL2L3Corrector
TrigReport          0          0          0          0          0 ak4TrackL2RelativeCorrector
TrigReport          0          0          0          0          0 ak4TrackL3AbsoluteCorrector
TrigReport          0          0          0          0          0 caloMetT1
TrigReport          0          0          0          0          0 caloMetT1T2
TrigReport          0          0          0          0          0 cleanPatElectrons
TrigReport          0          0          0          0          0 cleanPatJets
TrigReport          0          0          0          0          0 cleanPatJetsJESDown
TrigReport          0          0          0          0          0 cleanPatJetsJESUp
TrigReport          0          0          0          0          0 cleanPatJetsNominal
TrigReport          0          0          0          0          0 cleanPatJetsResnDown
TrigReport          0          0          0          0          0 cleanPatJetsResnUp
TrigReport          0          0          0          0          0 cleanPatMuons
TrigReport          0          0          0          0          0 cleanPatPhotons
TrigReport          0          0          0          0          0 cleanPatTaus
TrigReport          0          0          0          0          0 corrCaloMetType1
TrigReport          0          0          0          0          0 corrCaloMetType2
TrigReport          0          0          0          0          0 corrPfMetType1
TrigReport          0          0          0          0          0 corrPfMetType2
TrigReport          0          0          0          0          0 countPatElectrons
TrigReport          0          0          0          0          0 countPatJets
TrigReport          0          0          0          0          0 countPatLeptons
TrigReport          0          0          0          0          0 countPatMuons
TrigReport          0          0          0          0          0 countPatPhotons
TrigReport          0          0          0          0          0 countPatTaus
TrigReport          0          0          0          0          0 elPFIsoDepositChargedAllPAT
TrigReport          0          0          0          0          0 elPFIsoDepositChargedAllPFBRECO
TrigReport          0          0          0          0          0 elPFIsoDepositChargedPAT
TrigReport          0          0          0          0          0 elPFIsoDepositChargedPFBRECO
TrigReport          0          0          0          0          0 elPFIsoDepositGammaPAT
TrigReport          0          0          0          0          0 elPFIsoDepositGammaPFBRECO
TrigReport          0          0          0          0          0 elPFIsoDepositNeutralPAT
TrigReport          0          0          0          0          0 elPFIsoDepositNeutralPFBRECO
TrigReport          0          0          0          0          0 elPFIsoDepositPUPAT
TrigReport          0          0          0          0          0 elPFIsoDepositPUPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueCharged03NoPFId
TrigReport          0          0          0          0          0 elPFIsoValueCharged03NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueCharged03NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueCharged03PFId
TrigReport          0          0          0          0          0 elPFIsoValueCharged03PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueCharged03PFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueCharged04NoPFId
TrigReport          0          0          0          0          0 elPFIsoValueCharged04NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueCharged04NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueCharged04PFId
TrigReport          0          0          0          0          0 elPFIsoValueCharged04PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueCharged04PFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll03NoPFId
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll03NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll03NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll03PFId
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll03PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll03PFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll04NoPFId
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll04NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll04NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll04PFId
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll04PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueChargedAll04PFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueGamma03NoPFId
TrigReport          0          0          0          0          0 elPFIsoValueGamma03NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueGamma03NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueGamma03PFId
TrigReport          0          0          0          0          0 elPFIsoValueGamma03PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueGamma03PFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueGamma04NoPFId
TrigReport          0          0          0          0          0 elPFIsoValueGamma04NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueGamma04NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueGamma04PFId
TrigReport          0          0          0          0          0 elPFIsoValueGamma04PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueGamma04PFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueNeutral03NoPFId
TrigReport          0          0          0          0          0 elPFIsoValueNeutral03NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueNeutral03NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueNeutral03PFId
TrigReport          0          0          0          0          0 elPFIsoValueNeutral03PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueNeutral03PFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueNeutral04NoPFId
TrigReport          0          0          0          0          0 elPFIsoValueNeutral04NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueNeutral04NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValueNeutral04PFId
TrigReport          0          0          0          0          0 elPFIsoValueNeutral04PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValueNeutral04PFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValuePU03NoPFId
TrigReport          0          0          0          0          0 elPFIsoValuePU03NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValuePU03NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValuePU03PFId
TrigReport          0          0          0          0          0 elPFIsoValuePU03PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValuePU03PFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValuePU04NoPFId
TrigReport          0          0          0          0          0 elPFIsoValuePU04NoPFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValuePU04NoPFIdPFBRECO
TrigReport          0          0          0          0          0 elPFIsoValuePU04PFId
TrigReport          0          0          0          0          0 elPFIsoValuePU04PFIdPAT
TrigReport          0          0          0          0          0 elPFIsoValuePU04PFIdPFBRECO
TrigReport          0          0          0          0          0 electronMatch
TrigReport          0          0          0          0          0 hpsPFTauChargedIsoPtSum
TrigReport          0          0          0          0          0 hpsPFTauDiscriminationByLoosePileupWeightedIsolation3Hits
TrigReport          0          0          0          0          0 hpsPFTauDiscriminationByMediumPileupWeightedIsolation3Hits
TrigReport          0          0          0          0          0 hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone
TrigReport          0          0          0          0          0 hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits
TrigReport          0          0          0          0          0 hpsPFTauDiscriminationByRawPileupWeightedIsolation3Hits
TrigReport          0          0          0          0          0 hpsPFTauDiscriminationByTightPileupWeightedIsolation3Hits
TrigReport          0          0          0          0          0 hpsPFTauFootprintCorrection
TrigReport          0          0          0          0          0 hpsPFTauNeutralIsoPtSum
TrigReport          0          0          0          0          0 hpsPFTauNeutralIsoPtSumWeight
TrigReport          0          0          0          0          0 hpsPFTauPUcorrPtSum
TrigReport          0          0          0          0          0 hpsPFTauPhotonPtSumOutsideSignalCone
TrigReport          0          0          0          0          0 isoDeposits
TrigReport          0          0          0          0          0 kinFitTtSemiLepEvent
TrigReport          0          0          0          0          0 kinFitTtSemiLepEventJERDown
TrigReport          0          0          0          0          0 kinFitTtSemiLepEventJERUp
TrigReport          0          0          0          0          0 kinFitTtSemiLepEventJESDown
TrigReport          0          0          0          0          0 kinFitTtSemiLepEventJESUp
TrigReport          0          0          0          0          0 muCaloMetCorr
TrigReport          0          0          0          0          0 muPFIsoDepositChargedAllPAT
TrigReport          0          0          0          0          0 muPFIsoDepositChargedAllPFBRECO
TrigReport          0          0          0          0          0 muPFIsoDepositChargedPAT
TrigReport          0          0          0          0          0 muPFIsoDepositChargedPFBRECO
TrigReport          0          0          0          0          0 muPFIsoDepositGammaPAT
TrigReport          0          0          0          0          0 muPFIsoDepositGammaPFBRECO
TrigReport          0          0          0          0          0 muPFIsoDepositNeutralPAT
TrigReport          0          0          0          0          0 muPFIsoDepositNeutralPFBRECO
TrigReport          0          0          0          0          0 muPFIsoDepositPUPAT
TrigReport          0          0          0          0          0 muPFIsoDepositPUPFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueCharged03
TrigReport          0          0          0          0          0 muPFIsoValueCharged03PAT
TrigReport          0          0          0          0          0 muPFIsoValueCharged03PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueCharged04
TrigReport          0          0          0          0          0 muPFIsoValueCharged04PAT
TrigReport          0          0          0          0          0 muPFIsoValueCharged04PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueChargedAll03
TrigReport          0          0          0          0          0 muPFIsoValueChargedAll03PAT
TrigReport          0          0          0          0          0 muPFIsoValueChargedAll03PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueChargedAll04
TrigReport          0          0          0          0          0 muPFIsoValueChargedAll04PAT
TrigReport          0          0          0          0          0 muPFIsoValueChargedAll04PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueGamma03
TrigReport          0          0          0          0          0 muPFIsoValueGamma03PAT
TrigReport          0          0          0          0          0 muPFIsoValueGamma03PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueGamma04
TrigReport          0          0          0          0          0 muPFIsoValueGamma04PAT
TrigReport          0          0          0          0          0 muPFIsoValueGamma04PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueGammaHighThreshold03
TrigReport          0          0          0          0          0 muPFIsoValueGammaHighThreshold03PAT
TrigReport          0          0          0          0          0 muPFIsoValueGammaHighThreshold03PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueGammaHighThreshold04
TrigReport          0          0          0          0          0 muPFIsoValueGammaHighThreshold04PAT
TrigReport          0          0          0          0          0 muPFIsoValueGammaHighThreshold04PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueNeutral03
TrigReport          0          0          0          0          0 muPFIsoValueNeutral03PAT
TrigReport          0          0          0          0          0 muPFIsoValueNeutral03PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueNeutral04
TrigReport          0          0          0          0          0 muPFIsoValueNeutral04PAT
TrigReport          0          0          0          0          0 muPFIsoValueNeutral04PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueNeutralHighThreshold03
TrigReport          0          0          0          0          0 muPFIsoValueNeutralHighThreshold03PAT
TrigReport          0          0          0          0          0 muPFIsoValueNeutralHighThreshold03PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValueNeutralHighThreshold04
TrigReport          0          0          0          0          0 muPFIsoValueNeutralHighThreshold04PAT
TrigReport          0          0          0          0          0 muPFIsoValueNeutralHighThreshold04PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValuePU03
TrigReport          0          0          0          0          0 muPFIsoValuePU03PAT
TrigReport          0          0          0          0          0 muPFIsoValuePU03PFBRECO
TrigReport          0          0          0          0          0 muPFIsoValuePU04
TrigReport          0          0          0          0          0 muPFIsoValuePU04PAT
TrigReport          0          0          0          0          0 muPFIsoValuePU04PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueCharged03
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueCharged03PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueCharged03PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueCharged04
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueCharged04PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueCharged04PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueChargedAll03
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueChargedAll03PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueChargedAll03PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueChargedAll04
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueChargedAll04PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueChargedAll04PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGamma03
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGamma03PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGamma03PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGamma04
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGamma04PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGamma04PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGammaHighThreshold03
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGammaHighThreshold03PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGammaHighThreshold03PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGammaHighThreshold04
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGammaHighThreshold04PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueGammaHighThreshold04PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutral03
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutral03PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutral03PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutral04
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutral04PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutral04PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutralHighThreshold03
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutralHighThreshold03PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutralHighThreshold03PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutralHighThreshold04
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutralHighThreshold04PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValueNeutralHighThreshold04PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValuePU03
TrigReport          0          0          0          0          0 muPFMeanDRIsoValuePU03PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValuePU03PFBRECO
TrigReport          0          0          0          0          0 muPFMeanDRIsoValuePU04
TrigReport          0          0          0          0          0 muPFMeanDRIsoValuePU04PAT
TrigReport          0          0          0          0          0 muPFMeanDRIsoValuePU04PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueCharged03
TrigReport          0          0          0          0          0 muPFSumDRIsoValueCharged03PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueCharged03PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueCharged04
TrigReport          0          0          0          0          0 muPFSumDRIsoValueCharged04PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueCharged04PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueChargedAll03
TrigReport          0          0          0          0          0 muPFSumDRIsoValueChargedAll03PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueChargedAll03PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueChargedAll04
TrigReport          0          0          0          0          0 muPFSumDRIsoValueChargedAll04PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueChargedAll04PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGamma03
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGamma03PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGamma03PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGamma04
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGamma04PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGamma04PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGammaHighThreshold03
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGammaHighThreshold03PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGammaHighThreshold03PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGammaHighThreshold04
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGammaHighThreshold04PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueGammaHighThreshold04PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutral03
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutral03PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutral03PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutral04
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutral04PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutral04PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutralHighThreshold03
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutralHighThreshold03PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutralHighThreshold03PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutralHighThreshold04
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutralHighThreshold04PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValueNeutralHighThreshold04PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValuePU03
TrigReport          0          0          0          0          0 muPFSumDRIsoValuePU03PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValuePU03PFBRECO
TrigReport          0          0          0          0          0 muPFSumDRIsoValuePU04
TrigReport          0          0          0          0          0 muPFSumDRIsoValuePU04PAT
TrigReport          0          0          0          0          0 muPFSumDRIsoValuePU04PFBRECO
TrigReport          0          0          0          0          0 muonMatch
TrigReport          1          1          0          0          1 out
TrigReport          0          0          0          0          0 particleFlowPtrs
TrigReport          0          0          0          0          0 patElectrons
TrigReport          0          0          0          0          0 patHemispheres
TrigReport          0          0          0          0          0 patJetCharge
TrigReport          1          1          1          0          0 patJetCorrFactors
TrigReport          1          1          0          0          1 patJetFlavourAssociation
TrigReport          0          0          0          0          0 patJetFlavourAssociationLegacy
TrigReport          0          0          0          0          0 patJetGenJetMatch
TrigReport          0          0          0          0          0 patJetPartonAssociationLegacy
TrigReport          0          0          0          0          0 patJetPartonMatch
TrigReport          1          1          0          0          1 patJetPartons
TrigReport          0          0          0          0          0 patJetPartonsLegacy
TrigReport          1          1          0          0          1 patJets
TrigReport          0          0          0          0          0 patMETs
TrigReport          0          0          0          0          0 patMuons
TrigReport          0          0          0          0          0 patPhotons
TrigReport          0          0          0          0          0 patTaus
TrigReport          0          0          0          0          0 pfAllChargedHadronsPFBRECO
TrigReport          0          0          0          0          0 pfAllChargedParticlesPFBRECO
TrigReport          0          0          0          0          0 pfAllNeutralHadronsAndPhotonsPFBRECO
TrigReport          0          0          0          0          0 pfAllNeutralHadronsPFBRECO
TrigReport          0          0          0          0          0 pfAllPhotonsPFBRECO
TrigReport          0          0          0          0          0 pfCandMETcorr
TrigReport          0          0          0          0          0 pfCandsNotInJetsForMetCorr
TrigReport          0          0          0          0          0 pfCandsNotInJetsPtrForMetCorr
TrigReport          0          0          0          0          0 pfJetsPtrForMetCorr
TrigReport          0          0          0          0          0 pfMetT0pc
TrigReport          0          0          0          0          0 pfMetT0pcT1
TrigReport          0          0          0          0          0 pfMetT0pcT1T2Txy
TrigReport          0          0          0          0          0 pfMetT0pcT1Txy
TrigReport          0          0          0          0          0 pfMetT0pcTxy
TrigReport          0          0          0          0          0 pfMetT0rt
TrigReport          0          0          0          0          0 pfMetT0rtT1
TrigReport          0          0          0          0          0 pfMetT0rtT1T2
TrigReport          0          0          0          0          0 pfMetT0rtT1T2Txy
TrigReport          0          0          0          0          0 pfMetT0rtT1Txy
TrigReport          0          0          0          0          0 pfMetT0rtT2
TrigReport          0          0          0          0          0 pfMetT0rtTxy
TrigReport          0          0          0          0          0 pfMetT1
TrigReport          0          0          0          0          0 pfMetT1T2
TrigReport          0          0          0          0          0 pfMetT1T2Txy
TrigReport          0          0          0          0          0 pfMetT1Txy
TrigReport          0          0          0          0          0 pfMetTxy
TrigReport          0          0          0          0          0 pfNoJet
TrigReport          0          0          0          0          0 pfNoPileUpIsoPFBRECO
TrigReport          0          0          0          0          0 pfNoPileUpPFBRECO
TrigReport          0          0          0          0          0 pfPileUpAllChargedParticlesPFBRECO
TrigReport          0          0          0          0          0 pfPileUpIsoPFBRECO
TrigReport          0          0          0          0          0 pfPileUpPFBRECO
TrigReport          0          0          0          0          0 phPFIsoDepositChargedAllPAT
TrigReport          0          0          0          0          0 phPFIsoDepositChargedAllPFBRECO
TrigReport          0          0          0          0          0 phPFIsoDepositChargedPAT
TrigReport          0          0          0          0          0 phPFIsoDepositChargedPFBRECO
TrigReport          0          0          0          0          0 phPFIsoDepositGammaPAT
TrigReport          0          0          0          0          0 phPFIsoDepositGammaPFBRECO
TrigReport          0          0          0          0          0 phPFIsoDepositNeutralPAT
TrigReport          0          0          0          0          0 phPFIsoDepositNeutralPFBRECO
TrigReport          0          0          0          0          0 phPFIsoDepositPUPAT
TrigReport          0          0          0          0          0 phPFIsoDepositPUPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValueCharged03PFId
TrigReport          0          0          0          0          0 phPFIsoValueCharged03PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValueCharged03PFIdPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValueCharged04PFId
TrigReport          0          0          0          0          0 phPFIsoValueCharged04PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValueCharged04PFIdPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValueChargedAll03PFId
TrigReport          0          0          0          0          0 phPFIsoValueChargedAll03PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValueChargedAll03PFIdPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValueChargedAll04PFId
TrigReport          0          0          0          0          0 phPFIsoValueChargedAll04PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValueChargedAll04PFIdPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValueGamma03PFId
TrigReport          0          0          0          0          0 phPFIsoValueGamma03PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValueGamma03PFIdPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValueGamma04PFId
TrigReport          0          0          0          0          0 phPFIsoValueGamma04PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValueGamma04PFIdPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValueNeutral03PFId
TrigReport          0          0          0          0          0 phPFIsoValueNeutral03PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValueNeutral03PFIdPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValueNeutral04PFId
TrigReport          0          0          0          0          0 phPFIsoValueNeutral04PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValueNeutral04PFIdPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValuePU03PFId
TrigReport          0          0          0          0          0 phPFIsoValuePU03PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValuePU03PFIdPFBRECO
TrigReport          0          0          0          0          0 phPFIsoValuePU04PFId
TrigReport          0          0          0          0          0 phPFIsoValuePU04PFIdPAT
TrigReport          0          0          0          0          0 phPFIsoValuePU04PFIdPFBRECO
TrigReport          0          0          0          0          0 photonMatch
TrigReport          0          0          0          0          0 scaledJetEnergyDown
TrigReport          0          0          0          0          0 scaledJetEnergyNominal
TrigReport          0          0          0          0          0 scaledJetEnergyResnDown
TrigReport          0          0          0          0          0 scaledJetEnergyResnUp
TrigReport          0          0          0          0          0 scaledJetEnergyUp
TrigReport          0          0          0          0          0 selectedPatElectrons
TrigReport          0          0          0          0          0 selectedPatJets
TrigReport          0          0          0          0          0 selectedPatMuons
TrigReport          0          0          0          0          0 selectedPatPhotons
TrigReport          0          0          0          0          0 selectedPatTaus
TrigReport          0          0          0          0          0 tauGenJetMatch
TrigReport          0          0          0          0          0 tauGenJets
TrigReport          0          0          0          0          0 tauGenJetsSelectorAllHadrons
TrigReport          0          0          0          0          0 tauIsoDepositPFCandidates
TrigReport          0          0          0          0          0 tauIsoDepositPFChargedHadrons
TrigReport          0          0          0          0          0 tauIsoDepositPFGammas
TrigReport          0          0          0          0          0 tauIsoDepositPFNeutralHadrons
TrigReport          0          0          0          0          0 tauMatch

TimeReport ---------- Event  Summary ---[sec]----
TimeReport       event loop CPU/event = 1.363690
TimeReport      event loop Real/event = 3.160815
TimeReport     sum Streams Real/event = 1.304303
TimeReport efficiency CPU/Real/thread = 0.431436

TimeReport ---------- Path   Summary ---[Real sec]----
TimeReport  per event     per exec  Name
TimeReport  per event     per exec  Name

TimeReport -------End-Path   Summary ---[Real sec]----
TimeReport  per event     per exec  Name
TimeReport   0.099968     0.099968  outpath
TimeReport  per event     per exec  Name

TimeReport ------ Modules in End-Path: outpath ---[Real sec]----
TimeReport  per event    per visit  Name
TimeReport   0.000000     0.000000  out
TimeReport  per event    per visit  Name

TimeReport ---------- Module Summary ---[Real sec]----
TimeReport  per event     per exec    per visit  Name
TimeReport   0.000000     0.000000     0.000000  ak4CaloL1FastL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL1FastL2L3L6Corrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL1FastL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL1FastjetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL1L2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL1L2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL1OffsetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL2L3L6Corrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL2RelativeCorrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL3AbsoluteCorrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloL6SLBCorrector
TimeReport   0.000000     0.000000     0.000000  ak4CaloResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL1FastL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL1FastL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL1FastjetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL1L2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL1L2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL1OffsetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL2RelativeCorrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTL3AbsoluteCorrector
TimeReport   0.000000     0.000000     0.000000  ak4JPTResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4L1JPTOffsetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL1FastL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL1FastL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL1FastjetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL1L2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL1L2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL1OffsetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL2RelativeCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSL3AbsoluteCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFCHSResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL1FastL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL1FastL2L3L6Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL1FastL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL1FastjetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL1L2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL1L2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL1OffsetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL2L3L6Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL2RelativeCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL3AbsoluteCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFL6SLBCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL1FastL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL1FastL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL1FastjetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL1L2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL1L2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL1OffsetCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL2L3ResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL2RelativeCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiL3AbsoluteCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFPuppiResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4PFResidualCorrector
TimeReport   0.000000     0.000000     0.000000  ak4TrackL2L3Corrector
TimeReport   0.000000     0.000000     0.000000  ak4TrackL2RelativeCorrector
TimeReport   0.000000     0.000000     0.000000  ak4TrackL3AbsoluteCorrector
TimeReport   0.000000     0.000000     0.000000  caloMetT1
TimeReport   0.000000     0.000000     0.000000  caloMetT1T2
TimeReport   0.000000     0.000000     0.000000  cleanPatElectrons
TimeReport   0.000000     0.000000     0.000000  cleanPatJets
TimeReport   0.000000     0.000000     0.000000  cleanPatJetsJESDown
TimeReport   0.000000     0.000000     0.000000  cleanPatJetsJESUp
TimeReport   0.000000     0.000000     0.000000  cleanPatJetsNominal
TimeReport   0.000000     0.000000     0.000000  cleanPatJetsResnDown
TimeReport   0.000000     0.000000     0.000000  cleanPatJetsResnUp
TimeReport   0.000000     0.000000     0.000000  cleanPatMuons
TimeReport   0.000000     0.000000     0.000000  cleanPatPhotons
TimeReport   0.000000     0.000000     0.000000  cleanPatTaus
TimeReport   0.000000     0.000000     0.000000  corrCaloMetType1
TimeReport   0.000000     0.000000     0.000000  corrCaloMetType2
TimeReport   0.000000     0.000000     0.000000  corrPfMetType1
TimeReport   0.000000     0.000000     0.000000  corrPfMetType2
TimeReport   0.000000     0.000000     0.000000  countPatElectrons
TimeReport   0.000000     0.000000     0.000000  countPatJets
TimeReport   0.000000     0.000000     0.000000  countPatLeptons
TimeReport   0.000000     0.000000     0.000000  countPatMuons
TimeReport   0.000000     0.000000     0.000000  countPatPhotons
TimeReport   0.000000     0.000000     0.000000  countPatTaus
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositChargedAllPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositChargedAllPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositChargedPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositChargedPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositGammaPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositGammaPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositNeutralPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositNeutralPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositPUPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoDepositPUPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged03NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged03NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged03NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged03PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged04NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged04NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged04NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged04PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueCharged04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll03NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll03NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll03NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll03PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll04NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll04NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll04NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll04PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueChargedAll04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma03NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma03NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma03NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma03PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma04NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma04NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma04NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma04PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueGamma04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral03NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral03NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral03NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral03PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral04NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral04NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral04NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral04PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValueNeutral04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU03NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU03NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU03NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU03PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU04NoPFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU04NoPFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU04NoPFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU04PFId
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  elPFIsoValuePU04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  electronMatch
TimeReport   0.000000     0.000000     0.000000  hpsPFTauChargedIsoPtSum
TimeReport   0.000000     0.000000     0.000000  hpsPFTauDiscriminationByLoosePileupWeightedIsolation3Hits
TimeReport   0.000000     0.000000     0.000000  hpsPFTauDiscriminationByMediumPileupWeightedIsolation3Hits
TimeReport   0.000000     0.000000     0.000000  hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone
TimeReport   0.000000     0.000000     0.000000  hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits
TimeReport   0.000000     0.000000     0.000000  hpsPFTauDiscriminationByRawPileupWeightedIsolation3Hits
TimeReport   0.000000     0.000000     0.000000  hpsPFTauDiscriminationByTightPileupWeightedIsolation3Hits
TimeReport   0.000000     0.000000     0.000000  hpsPFTauFootprintCorrection
TimeReport   0.000000     0.000000     0.000000  hpsPFTauNeutralIsoPtSum
TimeReport   0.000000     0.000000     0.000000  hpsPFTauNeutralIsoPtSumWeight
TimeReport   0.000000     0.000000     0.000000  hpsPFTauPUcorrPtSum
TimeReport   0.000000     0.000000     0.000000  hpsPFTauPhotonPtSumOutsideSignalCone
TimeReport   0.000000     0.000000     0.000000  isoDeposits
TimeReport   0.000000     0.000000     0.000000  kinFitTtSemiLepEvent
TimeReport   0.000000     0.000000     0.000000  kinFitTtSemiLepEventJERDown
TimeReport   0.000000     0.000000     0.000000  kinFitTtSemiLepEventJERUp
TimeReport   0.000000     0.000000     0.000000  kinFitTtSemiLepEventJESDown
TimeReport   0.000000     0.000000     0.000000  kinFitTtSemiLepEventJESUp
TimeReport   0.000000     0.000000     0.000000  muCaloMetCorr
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositChargedAllPAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositChargedAllPFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositChargedPAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositChargedPFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositGammaPAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositGammaPFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositNeutralPAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositNeutralPFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositPUPAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoDepositPUPFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueCharged03
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueCharged03PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueCharged03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueCharged04
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueCharged04PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueCharged04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueChargedAll03
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueChargedAll03PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueChargedAll03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueChargedAll04
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueChargedAll04PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueChargedAll04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGamma03
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGamma03PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGamma03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGamma04
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGamma04PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGamma04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGammaHighThreshold03
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGammaHighThreshold03PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGammaHighThreshold03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGammaHighThreshold04
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGammaHighThreshold04PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueGammaHighThreshold04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutral03
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutral03PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutral03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutral04
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutral04PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutral04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutralHighThreshold03
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutralHighThreshold03PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutralHighThreshold03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutralHighThreshold04
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutralHighThreshold04PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValueNeutralHighThreshold04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValuePU03
TimeReport   0.000000     0.000000     0.000000  muPFIsoValuePU03PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValuePU03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFIsoValuePU04
TimeReport   0.000000     0.000000     0.000000  muPFIsoValuePU04PAT
TimeReport   0.000000     0.000000     0.000000  muPFIsoValuePU04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueCharged03
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueCharged03PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueCharged03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueCharged04
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueCharged04PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueCharged04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueChargedAll03
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueChargedAll03PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueChargedAll03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueChargedAll04
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueChargedAll04PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueChargedAll04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGamma03
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGamma03PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGamma03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGamma04
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGamma04PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGamma04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGammaHighThreshold03
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGammaHighThreshold03PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGammaHighThreshold03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGammaHighThreshold04
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGammaHighThreshold04PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueGammaHighThreshold04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutral03
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutral03PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutral03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutral04
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutral04PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutral04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutralHighThreshold03
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutralHighThreshold03PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutralHighThreshold03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutralHighThreshold04
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutralHighThreshold04PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValueNeutralHighThreshold04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValuePU03
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValuePU03PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValuePU03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValuePU04
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValuePU04PAT
TimeReport   0.000000     0.000000     0.000000  muPFMeanDRIsoValuePU04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueCharged03
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueCharged03PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueCharged03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueCharged04
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueCharged04PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueCharged04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueChargedAll03
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueChargedAll03PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueChargedAll03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueChargedAll04
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueChargedAll04PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueChargedAll04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGamma03
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGamma03PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGamma03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGamma04
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGamma04PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGamma04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGammaHighThreshold03
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGammaHighThreshold03PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGammaHighThreshold03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGammaHighThreshold04
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGammaHighThreshold04PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueGammaHighThreshold04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutral03
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutral03PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutral03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutral04
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutral04PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutral04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutralHighThreshold03
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutralHighThreshold03PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutralHighThreshold03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutralHighThreshold04
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutralHighThreshold04PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValueNeutralHighThreshold04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValuePU03
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValuePU03PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValuePU03PFBRECO
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValuePU04
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValuePU04PAT
TimeReport   0.000000     0.000000     0.000000  muPFSumDRIsoValuePU04PFBRECO
TimeReport   0.000000     0.000000     0.000000  muonMatch
TimeReport   0.850257     0.850257     0.850257  out
TimeReport   0.000000     0.000000     0.000000  particleFlowPtrs
TimeReport   0.000000     0.000000     0.000000  patElectrons
TimeReport   0.000000     0.000000     0.000000  patHemispheres
TimeReport   0.000000     0.000000     0.000000  patJetCharge
TimeReport   0.021186     0.021186     0.021186  patJetCorrFactors
TimeReport   0.851130     0.851130     0.851130  patJetFlavourAssociation
TimeReport   0.000000     0.000000     0.000000  patJetFlavourAssociationLegacy
TimeReport   0.000000     0.000000     0.000000  patJetGenJetMatch
TimeReport   0.000000     0.000000     0.000000  patJetPartonAssociationLegacy
TimeReport   0.000000     0.000000     0.000000  patJetPartonMatch
TimeReport   0.002130     0.002130     0.002130  patJetPartons
TimeReport   0.000000     0.000000     0.000000  patJetPartonsLegacy
TimeReport   0.000075     0.000075     0.000075  patJets
TimeReport   0.000000     0.000000     0.000000  patMETs
TimeReport   0.000000     0.000000     0.000000  patMuons
TimeReport   0.000000     0.000000     0.000000  patPhotons
TimeReport   0.000000     0.000000     0.000000  patTaus
TimeReport   0.000000     0.000000     0.000000  pfAllChargedHadronsPFBRECO
TimeReport   0.000000     0.000000     0.000000  pfAllChargedParticlesPFBRECO
TimeReport   0.000000     0.000000     0.000000  pfAllNeutralHadronsAndPhotonsPFBRECO
TimeReport   0.000000     0.000000     0.000000  pfAllNeutralHadronsPFBRECO
TimeReport   0.000000     0.000000     0.000000  pfAllPhotonsPFBRECO
TimeReport   0.000000     0.000000     0.000000  pfCandMETcorr
TimeReport   0.000000     0.000000     0.000000  pfCandsNotInJetsForMetCorr
TimeReport   0.000000     0.000000     0.000000  pfCandsNotInJetsPtrForMetCorr
TimeReport   0.000000     0.000000     0.000000  pfJetsPtrForMetCorr
TimeReport   0.000000     0.000000     0.000000  pfMetT0pc
TimeReport   0.000000     0.000000     0.000000  pfMetT0pcT1
TimeReport   0.000000     0.000000     0.000000  pfMetT0pcT1T2Txy
TimeReport   0.000000     0.000000     0.000000  pfMetT0pcT1Txy
TimeReport   0.000000     0.000000     0.000000  pfMetT0pcTxy
TimeReport   0.000000     0.000000     0.000000  pfMetT0rt
TimeReport   0.000000     0.000000     0.000000  pfMetT0rtT1
TimeReport   0.000000     0.000000     0.000000  pfMetT0rtT1T2
TimeReport   0.000000     0.000000     0.000000  pfMetT0rtT1T2Txy
TimeReport   0.000000     0.000000     0.000000  pfMetT0rtT1Txy
TimeReport   0.000000     0.000000     0.000000  pfMetT0rtT2
TimeReport   0.000000     0.000000     0.000000  pfMetT0rtTxy
TimeReport   0.000000     0.000000     0.000000  pfMetT1
TimeReport   0.000000     0.000000     0.000000  pfMetT1T2
TimeReport   0.000000     0.000000     0.000000  pfMetT1T2Txy
TimeReport   0.000000     0.000000     0.000000  pfMetT1Txy
TimeReport   0.000000     0.000000     0.000000  pfMetTxy
TimeReport   0.000000     0.000000     0.000000  pfNoJet
TimeReport   0.000000     0.000000     0.000000  pfNoPileUpIsoPFBRECO
TimeReport   0.000000     0.000000     0.000000  pfNoPileUpPFBRECO
TimeReport   0.000000     0.000000     0.000000  pfPileUpAllChargedParticlesPFBRECO
TimeReport   0.000000     0.000000     0.000000  pfPileUpIsoPFBRECO
TimeReport   0.000000     0.000000     0.000000  pfPileUpPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositChargedAllPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositChargedAllPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositChargedPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositChargedPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositGammaPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositGammaPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositNeutralPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositNeutralPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositPUPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoDepositPUPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueCharged03PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueCharged03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueCharged03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueCharged04PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueCharged04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueCharged04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueChargedAll03PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueChargedAll03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueChargedAll03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueChargedAll04PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueChargedAll04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueChargedAll04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueGamma03PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueGamma03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueGamma03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueGamma04PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueGamma04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueGamma04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueNeutral03PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueNeutral03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueNeutral03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueNeutral04PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueNeutral04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValueNeutral04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValuePU03PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValuePU03PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValuePU03PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  phPFIsoValuePU04PFId
TimeReport   0.000000     0.000000     0.000000  phPFIsoValuePU04PFIdPAT
TimeReport   0.000000     0.000000     0.000000  phPFIsoValuePU04PFIdPFBRECO
TimeReport   0.000000     0.000000     0.000000  photonMatch
TimeReport   0.000000     0.000000     0.000000  scaledJetEnergyDown
TimeReport   0.000000     0.000000     0.000000  scaledJetEnergyNominal
TimeReport   0.000000     0.000000     0.000000  scaledJetEnergyResnDown
TimeReport   0.000000     0.000000     0.000000  scaledJetEnergyResnUp
TimeReport   0.000000     0.000000     0.000000  scaledJetEnergyUp
TimeReport   0.000000     0.000000     0.000000  selectedPatElectrons
TimeReport   0.000000     0.000000     0.000000  selectedPatJets
TimeReport   0.000000     0.000000     0.000000  selectedPatMuons
TimeReport   0.000000     0.000000     0.000000  selectedPatPhotons
TimeReport   0.000000     0.000000     0.000000  selectedPatTaus
TimeReport   0.000000     0.000000     0.000000  tauGenJetMatch
TimeReport   0.000000     0.000000     0.000000  tauGenJets
TimeReport   0.000000     0.000000     0.000000  tauGenJetsSelectorAllHadrons
TimeReport   0.000000     0.000000     0.000000  tauIsoDepositPFCandidates
TimeReport   0.000000     0.000000     0.000000  tauIsoDepositPFChargedHadrons
TimeReport   0.000000     0.000000     0.000000  tauIsoDepositPFGammas
TimeReport   0.000000     0.000000     0.000000  tauIsoDepositPFNeutralHadrons
TimeReport   0.000000     0.000000     0.000000  tauMatch
TimeReport  per event     per exec    per visit  Name

T---Report end!


=============================================

MessageLogger Summary

 type     category        sev    module        subroutine        count    total
 ---- -------------------- -- ---------------- ----------------  -----    -----
    1 Fatal Exception      -s PostProcessPath                        1        1
    2 fileAction           -s file_close                             1        1
    3 fileAction           -s file_open                              2        2

 type    category    Examples: run/evt        run/evt          run/evt
 ---- -------------------- ---------------- ---------------- ----------------
    1 Fatal Exception      1/26354                           
    2 fileAction           PostEndRun                        
    3 fileAction           pre-events       pre-events       

Severity    # Occurrences   Total Occurrences
--------    -------------   -----------------
System                  4                   4
