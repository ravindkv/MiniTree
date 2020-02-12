import FWCore.ParameterSet.Config as cms

scaledJetEnergy = cms.EDProducer("JetEnergyScale",
    inputJets            = cms.InputTag("slimmedJets"),
    inputMETs            = cms.InputTag("slimmedMETs"),
    scaleType            = cms.string("abs"), #abs or rel(*eta) or jes:up / jes:down (pt-dependend)
    payload              = cms.string("AK4PF"), #jet and constituent type in JetMET convention
    jetPTThresholdForMET = cms.double(10.),
    jetEMLimitForMET     = cms.double(0.9),
    resolutionFactors    = cms.vdouble(1.0), # list the different JER factors here: (JER1, JER2)
    resolutionetaRangess  = cms.vdouble(0, -1)  # list the |eta| ranges for the different JER factors here (etaMin1, etaMax1, etaMin2, etaMax2), etaMax=-1: means |eta|<infinity
)

#####################################
# JER values used in KinFit
#New SF with stat + sys unc
#https://github.com/cms-jet/JRDatabase/blob/master/textFiles/Spring16_25nsV10a_MC/Spring16_25nsV10a_MC_SF_AK4PFchs.txt
#####################################
etaValues = []
etaRanges = []
jerSF     = []
jerSFUp   = []
jerSFDown = []

#Eta values
etaValues.append(0.0);
etaValues.append(0.5);
etaValues.append(0.8);
etaValues.append(1.1);
etaValues.append(1.3);
etaValues.append(1.7);
etaValues.append(1.9);
etaValues.append(2.1);
etaValues.append(2.3);
etaValues.append(2.5);
etaValues.append(2.8);
etaValues.append(3.0);
etaValues.append(3.2);
etaValues.append(-1);
#Eta range
etaRanges.append(0.0)
etaRanges.append(0.5)
etaRanges.append(0.5)
etaRanges.append(0.8)
etaRanges.append(0.8)
etaRanges.append(1.1)
etaRanges.append(1.1)
etaRanges.append(1.3)
etaRanges.append(1.3)
etaRanges.append(1.7)
etaRanges.append(1.7)
etaRanges.append(1.9)
etaRanges.append(1.9)
etaRanges.append(2.1)
etaRanges.append(2.1)
etaRanges.append(2.3)
etaRanges.append(2.3)
etaRanges.append(2.5)
etaRanges.append(2.5)
etaRanges.append(2.8)
etaRanges.append(2.8)
etaRanges.append(3.0)
etaRanges.append(3.0)
etaRanges.append(3.2)
etaRanges.append(3.2)
etaRanges.append(-1)
#SF values
jerSF.append(1.109); jerSFDown.append(1.044); jerSFUp.append(1.174);
jerSF.append(1.138); jerSFDown.append(1.072); jerSFUp.append(1.204);
jerSF.append(1.114); jerSFDown.append(1.050); jerSFUp.append(1.178);
jerSF.append(1.123); jerSFDown.append(1.022); jerSFUp.append(1.224);
jerSF.append(1.084); jerSFDown.append(0.985); jerSFUp.append(1.183);
jerSF.append(1.082); jerSFDown.append(0.973); jerSFUp.append(1.191);
jerSF.append(1.140); jerSFDown.append(1.020); jerSFUp.append(1.260);
jerSF.append(1.067); jerSFDown.append(0.953); jerSFUp.append(1.181);
jerSF.append(1.177); jerSFDown.append(0.967); jerSFUp.append(1.387);
jerSF.append(1.364); jerSFDown.append(1.203); jerSFUp.append(1.525);
jerSF.append(1.857); jerSFDown.append(1.654); jerSFUp.append(2.060);
jerSF.append(1.328); jerSFDown.append(1.203); jerSFUp.append(1.453);
jerSF.append(1.160); jerSFDown.append(1.013); jerSFUp.append(1.307);
