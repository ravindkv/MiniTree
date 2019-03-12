import FWCore.ParameterSet.Config as cms

scaledJetEnergy = cms.EDProducer("JetEnergyScale",
    inputJets            = cms.InputTag("slimmedJets"),
    inputMETs            = cms.InputTag("slimmedMETs"),
    scaleFactor          = cms.double(1.0),
    scaleFactorB         = cms.double(1.0),
    scaleType            = cms.string("abs"), #abs or rel(*eta) or jes:up / jes:down (pt-dependend)
    payload              = cms.string("AK4PFchs"), #jet and constituent type in JetMET convention
    jetPTThresholdForMET = cms.double(10.),
    jetEMLimitForMET     = cms.double(0.9),
    resolutionFactors    = cms.vdouble(1.0), # list the different JER factors here: (JER1, JER2)
    resolutionetaRangess  = cms.vdouble(0, -1),  # list the |eta| ranges for the different JER factors here (etaMin1, etaMax1, etaMin2, etaMax2), etaMax=-1: means |eta|<infinity
    JECUncSrcFile        = cms.FileInPath("MiniTree/Selection/data/80X_mcRun2_asymptotic_2016_TrancheIV_v8_Uncertainty_AK4PFchs.txt"),
    resolutionsFile   = cms.FileInPath("MiniTree/Selection/data/Summer16_25nsV1_MC_PtResolution_AK4PF.txt"),
    scaleFactorsFile  = cms.FileInPath("MiniTree/Selection/data/Summer16_25nsV1_MC_SF_AK4PF.txt")
)

# JER values used in KinFit
# https://github.com/cms-jet/JRDatabase/blob/master/textFiles/Summer16_25nsV1_MC/Summer16_25nsV1_MC_SF_AK4PF.txt
etaValues = []
etaRanges = []
jerSF     = []
jerSFUp   = []
jerSFDown = []
#Eta values
etaValues.append(0.000);
etaValues.append(0.522);
etaValues.append(0.783);
etaValues.append(1.131);
etaValues.append(1.305);
etaValues.append(1.740);
etaValues.append(1.930);
etaValues.append(2.043);
etaValues.append(2.322);
etaValues.append(2.500);
etaValues.append(2.853);
etaValues.append(2.964);
etaValues.append(3.139);
etaValues.append(5.191);
#Eta range
etaRanges.append(0.000)
etaRanges.append(0.522)
etaRanges.append(0.522)
etaRanges.append(0.783)
etaRanges.append(0.783)
etaRanges.append(1.131)
etaRanges.append(1.131)
etaRanges.append(1.305)
etaRanges.append(1.305)
etaRanges.append(1.740)
etaRanges.append(1.740)
etaRanges.append(1.930)
etaRanges.append(1.930)
etaRanges.append(2.043)
etaRanges.append(2.043)
etaRanges.append(2.322)
etaRanges.append(2.322)
etaRanges.append(2.500)
etaRanges.append(2.500)
etaRanges.append(2.853)
etaRanges.append(2.853)
etaRanges.append(2.964)
etaRanges.append(2.964)
etaRanges.append(3.139)
etaRanges.append(3.139)
etaRanges.append(-1)
#SF values
jerSF.append(1.1595); jerSFDown.append(1.095);  jerSFUp.append(1.224);
jerSF.append(1.1948); jerSFDown.append(1.1296); jerSFUp.append(1.26);
jerSF.append(1.1464); jerSFDown.append(1.0832); jerSFUp.append(1.2096);
jerSF.append(1.1609); jerSFDown.append(1.0584); jerSFUp.append(1.2634);
jerSF.append(1.1278); jerSFDown.append(1.0292); jerSFUp.append(1.2264);
jerSF.append(1.1000); jerSFDown.append(0.9921); jerSFUp.append(1.2079);
jerSF.append(1.1426); jerSFDown.append(1.0212); jerSFUp.append(1.264);
jerSF.append(1.1512); jerSFDown.append(1.0372); jerSFUp.append(1.2652);
jerSF.append(1.2963); jerSFDown.append(1.0592); jerSFUp.append(1.5334);
jerSF.append(1.3418); jerSFDown.append(1.1327); jerSFUp.append(1.5509);
jerSF.append(1.7788); jerSFDown.append(1.578);  jerSFUp.append(1.9796);
jerSF.append(1.1869); jerSFDown.append(1.0626); jerSFUp.append(1.3112);
jerSF.append(1.1922); jerSFDown.append(1.0434); jerSFUp.append(1.341);
