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
#https://github.com/cms-jet/JRDatabase/blob/master/textFiles/Spring16_25nsV6a_MC/Spring16_25nsV6a_MC_SF_AK4PF.txt
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
jerSF.append(1.122); jerSFDown.append(1.053); jerSFUp.append(1.191);
jerSF.append(1.167); jerSFDown.append(1.087); jerSFUp.append(1.247);
jerSF.append(1.168); jerSFDown.append(1.090); jerSFUp.append(1.246);
jerSF.append(1.029); jerSFDown.append(0.911); jerSFUp.append(1.147);
jerSF.append(1.115); jerSFDown.append(1.013); jerSFUp.append(1.217);
jerSF.append(1.041); jerSFDown.append(0.921); jerSFUp.append(1.161);
jerSF.append(1.167); jerSFDown.append(1.027); jerSFUp.append(1.307);
jerSF.append(1.094); jerSFDown.append(0.957); jerSFUp.append(1.231);
jerSF.append(1.168); jerSFDown.append(0.929); jerSFUp.append(1.407);
jerSF.append(1.266); jerSFDown.append(1.062); jerSFUp.append(1.470);
jerSF.append(1.595); jerSFDown.append(1.337); jerSFUp.append(1.853);
jerSF.append(0.998); jerSFDown.append(0.859); jerSFUp.append(1.137);
jerSF.append(1.226); jerSFDown.append(1.022); jerSFUp.append(1.430);
