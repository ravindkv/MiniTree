#include "MiniTree/Selection/interface/MyJet.h"

MyJet::MyJet():
  
  ///basic  
  jetCharge(0),
  jetName(""),
  parton_id(0),
  parton_mother_id(0),
  partonFlavour(0),

  ///ids
  neutralHadronEnergyFraction(999.),
  neutralEmEnergyFraction(999.),
  NumConst(0.),
  muonEnergyFraction(999.),
  chargedHadronEnergyFraction(999.),
  chargedMultiplicity(0.),
  chargedEmEnergyFraction(999.),
  neutralMultiplicity(0.),
  jetIDLoose(false),
  
  ///JEC
  JECUncertainty(999.),
  triggerJet_pt(999.),
  quality(0)
{
}

MyJet::~MyJet() 
{
}

void MyJet::Reset()
{
  ///basic
  Genp4.SetCoordinates(0.0, 0.0, 0.0, 0.0);
  jetCharge = 0;
  jetName = "";
  p4.SetCoordinates(0.0, 0.0, 0.0, 0.0);
  parton_id = 0;
  parton_mother_id = 0;
  partonFlavour = 0;
  vertex.SetCoordinates(-999.0,-999.0,-999.0);

  ///ids
  neutralHadronEnergyFraction = 999.;
  neutralEmEnergyFraction = 999.;
  NumConst = 0.;
  muonEnergyFraction = 999.;
  chargedHadronEnergyFraction = 999.;
  chargedMultiplicity = 0.;
  chargedEmEnergyFraction = 999.;
  neutralMultiplicity = 0.;
  jetIDLoose = false;
  
  ///btag, JEC, SV
  bDiscriminator.clear();
  JECs.clear();
  JECUncertainty = 999.;
  SVP4.clear();
  SVflightDistance.clear();
  SVflightDistanceErr.clear();
  SVNChi2.clear();

  triggerJet_pt = 0.;
  quality = 0;

}
