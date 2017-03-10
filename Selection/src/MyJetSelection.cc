#include "MiniTree/Selection/interface/MyEventSelection.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
//#include "CMGTools/External/interface/PileupJetIdentifier.h"
#include "DataFormats/BTauReco/interface/SecondaryVertexTagInfo.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

std::vector<MyJet> MyEventSelection::getJets(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std; 
  std::vector<MyJet> selJets; 
  selJets.clear();
  
  jetIDFunctor_ = JetIDSelectionFunctor(configParamsJets_.getParameter<edm::ParameterSet>("CaloJetId") );
  pfjetIDFunctor_ = PFJetIDSelectionFunctor(configParamsJets_.getParameter<edm::ParameterSet>("PFJetId") );
  
  // jet ID handle
  //edm::Handle<reco::JetIDValueMap> hJetIDMap; // already defined in MyEventSelection.h
  iEvent.getByToken( jetIDMapToken_, hJetIDMap ); // 76x
  
  try{
    //config parameters
    double minPt = configParamsJets_.getParameter<double>("minPt");
    double maxEta = configParamsJets_.getParameter<double>("maxEta");
    try{ 
      //      iEvent.getByLabel(puMVADiscriminantResCor, puJetIdMVARC);
      //      iEvent.getByLabel(puMVAIDResCor, puJetIdFlagRC);
    }catch(std::exception &e){ 
    }
    
    TString rawtag="Jets";
    //std::string tag(rawtag);
    TString tag(rawtag);
    
    edm::Handle<pat::JetCollection>ijets;
    iEvent.getByToken( Jetsources, ijets); // 76x
    if(ijets.isValid()){
      
      edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
      //get the jet corrector parameters collection from the globaltag
      std::string uncType("PF");
      if(rawtag.Contains("JPT") ) uncType="JPT";
      else if(rawtag.Contains("Calo") ) uncType="Calo";
      else if(rawtag.Contains("TRK") ) uncType="TRK";
      iSetup.get<JetCorrectionsRecord>().get("AK5"+uncType,JetCorParColl);
      // get the uncertainty parameters from the collection
      JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"]; 
      // instantiate the jec uncertainty object
      JetCorrectionUncertainty *jecUnc = new JetCorrectionUncertainty(JetCorPar); 
      
      for(size_t iJet = 0; iJet < ijets->size(); iJet++)
	{
	  const pat::Jet jIt = ((*ijets)[iJet]);
	  
	  if(jIt.pt() < 15 || fabs(jIt.eta()) > maxEta)continue;
	  
	  MyJet newJet = MyJetConverter(jIt, rawtag);
	  newJet.jetName = tag;
	  
	  //JEC uncertainty
	  jecUnc->setJetEta(jIt.eta());
	  jecUnc->setJetPt(jIt.pt());  
	  float JECUncertainty = jecUnc->getUncertainty(true);
	  newJet.JECUncertainty = JECUncertainty;
	  
	  //make selections
	  bool passKin = true, passId = true, passIso = true;
	  if(jIt.pt() < minPt || fabs(jIt.eta()) > maxEta)passKin = false;
	  
      //ids
	  ///if(!(newJet.jetIDLoose))passId = false;
          	  
	  int quality = 0;
	  if(passKin)quality  = 1;
	  //std::cout<<"jet quality "<<quality<<std::endl;
	  if(passId)quality |= 1<<1;
	  //std::cout<<"jet quality "<<quality<<std::endl;
	  if(passIso)quality |= 1<<2;
	  //std::cout<<"jet quality "<<quality<<std::endl;
	  newJet.quality = quality;
	  
	  if(passKin && passId) selJets.push_back(newJet);
    } // for loop
      delete jecUnc;
      fs_->cd();
	}
  }catch(std::exception &e){
    std::cout << "[Jet Selection] : check selection " << e.what() << std::endl;
  }
  
  return selJets;
}


MyJet MyEventSelection::MyJetConverter(const pat::Jet& iJet, TString& dirtag)
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

  newJet.partonFlavour = double(iJet.partonFlavour());
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
  std::map<std::string, double>jetCorrections; jetCorrections.clear();
  const std::vector<std::string> jeclevels = iJet.availableJECLevels();
  for(size_t j = 0; j < jeclevels.size(); j++){
    std::string levelName = jeclevels[j];
    if(levelName.find("L5Flavor") != std::string::npos ||
       levelName.find("L7Parton") != std::string::npos ){
      jetCorrections[levelName] = iJet.jecFactor(levelName, "bottom");
    }
    else{ jetCorrections[levelName] = iJet.jecFactor(levelName); }
  }
  newJet.JECs = jetCorrections;
  newJet.JECUncertainty = 1.0;  //default, get it later from CondDB.
  //SV
  const reco::SecondaryVertexTagInfo *svTagInfo = iJet.tagInfoSecondaryVertex();
  //https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookChapter7
  //const reco::SecondaryVertexTagInfo *svTagInfo = iJet.tagInfoSecondaryVertex("secondaryVertex");
  if(svTagInfo){
    for(size_t iv = 0; iv < svTagInfo->nVertices(); iv++){
      const reco::Vertex& sv = svTagInfo->secondaryVertex(iv);
      if(!(sv.isFake())){
	newJet.SVP4.push_back(sv.p4());
	newJet.SVflightDistance.push_back(svTagInfo->flightDistance(iv).value());
	newJet.SVflightDistanceErr.push_back(svTagInfo->flightDistance(iv).error());
	newJet.SVNChi2.push_back(sv.normalizedChi2());
      }
    }
  }
  //jet id
  return newJet;
}

