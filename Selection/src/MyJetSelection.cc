#include "MiniTree/Selection/interface/MyEventSelection.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/BTauReco/interface/SecondaryVertexTagInfo.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

std::vector<MyJet> MyEventSelection::getJets(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std; 
  std::vector<MyJet> selJets; 
  selJets.clear();
  try{
    //config parameters
    double minPt = configParamsJets_.getParameter<double>("minPt");
    double maxEta = configParamsJets_.getParameter<double>("maxEta");
    
    TString rawtag="Jets";
    //std::string tag(rawtag);
    TString tag(rawtag);
    
    edm::Handle<pat::JetCollection>ijets;
    iEvent.getByToken( Jetsources, ijets);  
    //Jet resolution and scale factors
    //https://github.com/cms-jet/JRDatabase/tree/master/textFiles/Spring16_25nsV10_MC
    //https://insight.io/github.com/cms-sw/cmssw/blob/master/JetMETCorrections/Modules/plugins/JetResolutionDemo.cc
    edm::Handle<double> rho;
    iEvent.getByToken(m_rho_token, rho);
    JME::JetResolution resolution;
    resolution = JME::JetResolution(m_resolutions_file);
    ///std::cout<<"m_resolutions_file = "<<m_resolutions_file<<std::endl;
    
    if(ijets.isValid()){
      edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
      //get the jet corrector parameters collection from the globaltag
      std::string uncType("AK4PFchs");
      iSetup.get<JetCorrectionsRecord>().get(uncType,JetCorParColl);
      // get the uncertainty parameters from the collection
      JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"]; 
      // instantiate the jec uncertainty object
      JetCorrectionUncertainty *jecUnc = new JetCorrectionUncertainty(JetCorPar); 
      
      for(size_t iJet = 0; iJet < ijets->size(); iJet++){
        const pat::Jet jIt = ((*ijets)[iJet]);
        //Jet resolution and scale factors
        JME::JetParameters parameters_5 = {{JME::Binning::JetPt, jIt.pt()}, {JME::Binning::JetEta, jIt.eta()}, {JME::Binning::Rho, *rho}};
        float reso = resolution.getResolution(parameters_5);
        //std::cout<<"resolutions = "<<reso<<std::endl;
        MyJet newJet = MyJetConverter(jIt, rawtag, reso);
        newJet.jetName = tag;
        newJet.scaleFactor = 1.0;
        newJet.resolution = reso; 
        
        //JEC uncertainty
        jecUnc->setJetEta(jIt.eta());
        jecUnc->setJetPt(jIt.pt());  
        float JECUncertainty = jecUnc->getUncertainty(true);
        newJet.JECUncertainty = JECUncertainty;
        //make selections
        bool passKin = true;
        if(jIt.pt() < minPt || fabs(jIt.eta()) > maxEta)passKin = false;
        if(passKin) selJets.push_back(newJet);
      } // for loop
      delete jecUnc;
      fs_->cd();
	}
  }catch(std::exception &e){
    std::cout << "[Jet Selection] : check selection " << e.what() << std::endl;
  }
  return selJets;
}

MyJet MyEventSelection::MyJetConverter(const pat::Jet& iJet, TString& dirtag, double JER)
{
  MyJet newJet;
  newJet.Reset();
  ///basic
  const reco::GenJet *genJet = iJet.genJet();
  if(genJet){
    newJet.Genp4.SetCoordinates(genJet->px(), genJet->py(), genJet->pz(), genJet->energy());
  }
  newJet.jetCharge = iJet.jetCharge();
  newJet.p4.SetCoordinates(iJet.px(), iJet.py(), iJet.pz(), iJet.energy());
  //MC truth
  const reco::GenParticle *genParton = iJet.genParton();
  newJet.parton_id = (genParton != 0 ? genParton->pdgId() : 0 );
  if(genParton){
    if(genParton->numberOfMothers() > 0){
      newJet.parton_mother_id = genParton->mother()->pdgId();
    }
  }
  myhistos_["pt_"+dirtag]->Fill(iJet.pt());
  myhistos_["eta_"+dirtag]->Fill(iJet.eta());
  myhistos_["phi_"+dirtag]->Fill(iJet.phi());
  myhistos_["JER_"+dirtag]->Fill(JER);
  
  newJet.partonFlavour = double(iJet.partonFlavour());
  newJet.hadronFlavour = double(iJet.hadronFlavour());
  
  //https://github.com/rappoccio/usercode/blob/Dev_53x/EDSHyFT/plugins/BTaggingEffAnalyzer.cc
  //2D histos to calculate Btag efficiency
  double partonFlavor = newJet.partonFlavour;
  double csv = iJet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags");
  double csvL = 0.5426;
  double csvM = 0.8484;
  double csvT = 0.9535;
  //b-quarks
  if( abs(partonFlavor)==5 ){
    myhistos2_["h2_BTagEff_Denom_b_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( csv > csvL ) myhistos2_["h2_BTagEff_Num_bL_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( csv > csvM ) myhistos2_["h2_BTagEff_Num_bM_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( csv > csvT ) myhistos2_["h2_BTagEff_Num_bT_"+dirtag]->Fill(iJet.pt(), iJet.eta());
  }
  //c-quarks
  else if( abs(partonFlavor)==4 ){
    myhistos2_["h2_BTagEff_Denom_c_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( csv > csvL ) myhistos2_["h2_BTagEff_Num_cL_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( csv > csvM ) myhistos2_["h2_BTagEff_Num_cM_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( csv > csvT ) myhistos2_["h2_BTagEff_Num_cT_"+dirtag]->Fill(iJet.pt(), iJet.eta());
  }
  //other quarks and gluon
  else{
    myhistos2_["h2_BTagEff_Denom_udsg_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( csv > csvL ) myhistos2_["h2_BTagEff_Num_udsgL_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( csv > csvM ) myhistos2_["h2_BTagEff_Num_udsgM_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( csv > csvT ) myhistos2_["h2_BTagEff_Num_udsgT_"+dirtag]->Fill(iJet.pt(), iJet.eta());
  }
 
  //2D histos to calculate Ctag efficiency
  double dCvsL = iJet.bDiscriminator("pfCombinedCvsLJetTags");
  double dCvsB = iJet.bDiscriminator("pfCombinedCvsBJetTags");
  double dCvsL_L = -0.48;
  double dCvsB_L = -0.17;
  double dCvsL_M = -0.1;
  double dCvsB_M =  0.08;
  double dCvsL_T =  0.69;
  double dCvsB_T = -0.45;
  //b-quarks
  if( abs(partonFlavor)==5 ){
    myhistos2_["h2_CTagEff_Denom_b_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( dCvsL > dCvsL_L && dCvsB > dCvsB_L) myhistos2_["h2_CTagEff_Num_bL_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( dCvsL > dCvsL_M && dCvsB > dCvsB_M) myhistos2_["h2_CTagEff_Num_bM_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( dCvsL > dCvsL_T && dCvsB > dCvsB_T) myhistos2_["h2_CTagEff_Num_bT_"+dirtag]->Fill(iJet.pt(), iJet.eta());
  }
  //c-quarks
  else if( abs(partonFlavor)==4 ){
    myhistos2_["h2_CTagEff_Denom_c_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( dCvsL > dCvsL_L && dCvsB > dCvsB_L) myhistos2_["h2_CTagEff_Num_cL_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( dCvsL > dCvsL_M && dCvsB > dCvsB_M) myhistos2_["h2_CTagEff_Num_cM_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( dCvsL > dCvsL_T && dCvsB > dCvsB_T) myhistos2_["h2_CTagEff_Num_cT_"+dirtag]->Fill(iJet.pt(), iJet.eta());
  }
  //other quarks and gluon
  else{
    myhistos2_["h2_CTagEff_Denom_udsg_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( dCvsL > dCvsL_L && dCvsB > dCvsB_L) myhistos2_["h2_CTagEff_Num_udsgL_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( dCvsL > dCvsL_M && dCvsB > dCvsB_M) myhistos2_["h2_CTagEff_Num_udsgM_"+dirtag]->Fill(iJet.pt(), iJet.eta());
    if( dCvsL > dCvsL_T && dCvsB > dCvsB_T) myhistos2_["h2_CTagEff_Num_udsgT_"+dirtag]->Fill(iJet.pt(), iJet.eta());
  }
  //vertex.fCoordinates.fXYZ are zero, in the MINIAOD
  newJet.vertex.SetCoordinates(iJet.vx(), iJet.vy(), iJet.vz());
  
  ///ids
  if(iJet.isPFJet())
    {     
      newJet.neutralHadronEnergyFraction = iJet.neutralHadronEnergyFraction(); 
      newJet.neutralEmEnergyFraction = iJet.neutralEmEnergyFraction();
      newJet.NumConst = iJet.chargedMultiplicity()+ iJet.neutralMultiplicity();
      newJet.muonEnergyFraction = iJet.muonEnergyFraction();
      newJet.chargedHadronEnergyFraction = iJet.chargedHadronEnergyFraction();
      newJet.chargedMultiplicity = iJet.chargedMultiplicity();
      newJet.chargedEmEnergyFraction = iJet.chargedEmEnergyFraction();
      newJet.neutralMultiplicity = iJet.neutralMultiplicity();
      myhistos_["emf_"+dirtag]->Fill(iJet.chargedEmEnergyFraction() + iJet.neutralEmEnergyFraction());
    }

  ///btag, JEC & SV
  //btag : https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
  std::map<std::string, double> discr; discr.clear();
  discr["pfCombinedInclusiveSecondaryVertexV2BJetTags"] = iJet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags");
  discr["pfCombinedMVAV2BJetTags"] = iJet.bDiscriminator("pfCombinedMVAV2BJetTags");
  discr["pfCombinedCvsLJetTags"] = iJet.bDiscriminator("pfCombinedCvsLJetTags");   
  discr["pfCombinedCvsBJetTags"] = iJet.bDiscriminator("pfCombinedCvsBJetTags");
  newJet.bDiscriminator = discr;

  //JECs
  std::map<std::string, double>jetCorrections; 
  jetCorrections.clear();
  const std::vector<std::string> jeclevels = iJet.availableJECLevels();
  for(size_t j = 0; j < jeclevels.size(); j++){
    std::string levelName = jeclevels[j];
    if(levelName.find("L5Flavor") != std::string::npos ||
       levelName.find("L7Parton") != std::string::npos ){
      jetCorrections[levelName] = iJet.jecFactor(levelName, "bottom");
    }
    else{ jetCorrections[levelName] = iJet.jecFactor(levelName); }
    //std::cout<<levelName<<": "<<iJet.jecFactor(levelName)<<std::endl;
  }
  newJet.JECs = jetCorrections;

  //jet id
  return newJet;
}

