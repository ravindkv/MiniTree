#include "MiniTree/Selection/interface/MyEventSelection.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"

// ---- 13 TeV
#include "PhysicsTools/SelectorUtils/interface/CutApplicatorWithEventContentBase.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"

std::vector<MyElectron> MyEventSelection::getElectrons(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std; 
  std::vector<MyElectron> selElectrons; 
  selElectrons.clear();
  
  try{
    std::string id = configParamsElectrons_.getParameter<std::string>("id");
    double maxRelIso = configParamsElectrons_.getParameter<double>("maxRelIso");
    double minEt = configParamsElectrons_.getParameter<double>("minEt");
    double maxEta = configParamsElectrons_.getParameter<double>("maxEta");
    double mvacut = configParamsElectrons_.getParameter<double>("mvacut");
    
    TString rawtag="Electrons";
    TString tag(rawtag);
    //std::string tag(rawtag);
    edm::Handle<pat::ElectronCollection>ieles;
    iEvent.getByToken(Elesources, ieles); 
    
    if(ieles.isValid()){
      for(size_t iEle = 0; iEle < ieles->size(); iEle++)
	{
	  const pat::Electron eIt = ((*ieles)[iEle]);
      
	  MyElectron newElectron = MyElectronConverter(eIt, rawtag);

      newElectron.eleName = tag; ///Memory leak
	  
	  //make selections
      bool passKin = true, passId = true, passIso = true;
	  if(newElectron.p4.Et() < minEt || 
	     fabs(newElectron.p4.Eta()) > maxEta) passKin = false;
	  
      //apply mva Id
	  double mvaid = eIt.electronID(id);
	  if(mvaid < mvacut) passId = false;
	  //if(newElectron.nMissingHits != 0) passId = false;
	  
      //iso
      if(newElectron.pfRelIso > maxRelIso) passIso = false;
	  int quality = 0;
	  if(passKin)quality  = 1;
      if(passId)quality |= 1<<1;
	  if(passIso)quality |= 1<<2;
	  newElectron.quality = quality;
	  
	  if(passKin)selElectrons.push_back(newElectron);
      selElectrons.push_back(newElectron);
    }//for loop
    }
    }catch(std::exception &e){
    std::cout << "[Electron Selection] : check selection " << e.what() << std::endl;
  }  
  return selElectrons;
}

    
MyElectron MyEventSelection::MyElectronConverter(const pat::Electron& iEle, TString& dirtag)
{
  MyElectron newElectron;
  newElectron.Reset();
  ///basic
  newElectron.charge = iEle.charge(); 
  const reco::GenParticle *gen = iEle.genLepton();
  if(gen){
    newElectron.gen_id = gen->pdgId();
    if(gen->numberOfMothers() > 0)
      newElectron.gen_mother_id = gen->mother()->pdgId();
  }
  newElectron.p4.SetCoordinates(iEle.px(), iEle.py(), iEle.pz(), iEle.energy());
  newElectron.vertex.SetCoordinates(iEle.vx(), iEle.vy(), iEle.vz());
  myhistos_["pt_"+dirtag]->Fill(iEle.pt());
  myhistos_["eta_"+dirtag]->Fill(iEle.eta());
  myhistos_["phi_"+dirtag]->Fill(iEle.phi());
  
  ///sel 
  newElectron.sigmaIetaIeta = iEle.full5x5_sigmaIetaIeta();
  //abs(dEtaInSeed)
  newElectron.dEtaInSeed = iEle.superCluster().isNonnull() && iEle.superCluster()->seed().isNonnull() ?iEle.deltaEtaSuperClusterTrackAtVtx() - iEle.superCluster()->eta() + iEle.superCluster()->seed()->eta() : std::numeric_limits<float>::max();
  //abs(dPhiIn)
  newElectron.dPhiIn = iEle.deltaPhiSuperClusterTrackAtVtx();
  newElectron.hadOverEm = iEle.hadronicOverEm();
  //Rel. comb. PF iso with EA corr
  //const reco::GsfElectron::PflowIsolationVariables& pfIso = iEle.pfIsolationVariables();
   //const float chad = pfIso.sumChargedHadronPt;
   //const float nhad = pfIso.sumNeutralHadronEt;
   //const float pho = pfIso.sumPhotonEt;
   //const float  eA = _effectiveAreas.getEffectiveArea( absEta );
   //const float rho = _rhoHandle.isValid() ? (float)(*_rhoHandle) : 0; // std::max likes float arguments
   //const float iso = chad + std::max(0.0f, nhad + pho - rho*eA);
   //const float iso = chad + std::max(0.0f, nhad + pho);
  //abs(1/E-1/p) 
  const float ecal_energy_inverse = 1.0/iEle.ecalEnergy();
  const float eSCoverP = iEle.eSuperClusterOverP();
  newElectron.iEminusiP = std::abs(1.0 - eSCoverP)*ecal_energy_inverse;
  //expected missing inner hits
  constexpr reco::HitPattern::HitCategory missingHitType = reco::HitPattern::MISSING_INNER_HITS;
  newElectron.nInnerHits = iEle.gsfTrack()->hitPattern().numberOfHits(missingHitType); 
  //pass conversion veto
  newElectron.isPassConVeto = iEle.passConversionVeto();
  
  ///ids
  newElectron.isEE = iEle.isEB();
  newElectron.isEB = iEle.isEE();
  std::map<std::string, float> eidWPs; eidWPs.clear();
  newElectron.eidWPs = eidWPs;
  
  ///iso
  std::vector<double> pfiso = defaultPFElectronIsolation(iEle);
  newElectron.ChHadIso = pfiso[0]; 
  newElectron.PhotonIso = pfiso[1];  
  newElectron.NeuHadIso = pfiso[2];  
  newElectron.PileupIso = pfiso[3];
  newElectron.D0 = iEle.gsfTrack()->dxy(refVertex_.position());
  newElectron.Dz = iEle.gsfTrack()->dz(refVertex_.position());
  myhistos_["pfRelIso_"+dirtag]->Fill(pfiso[4]); 
  return newElectron;
}

std::vector<double> MyEventSelection::defaultPFElectronIsolation (const pat::Electron& ele)
{
  double ePt((double)ele.pt());
  double norm=std::max((double)20.0,(double)ePt);
  double puOffsetCorrection = 0.0;
  std::vector<double> values(4,0);
    values[0] = ele.chargedHadronIso();
    values[1] = ele.photonIso();
    values[2] = ele.neutralHadronIso();
    values[3] =(std::max(ele.photonIso()+ele.neutralHadronIso() - puOffsetCorrection, 0.0) + ele.chargedHadronIso())/norm;

    return values;
}
