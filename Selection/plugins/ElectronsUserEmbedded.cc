#ifndef LLRAnalysis_TauTauStudies_ElectronsUserEmbedded_h
#define LLRAnalysis_TauTauStudies_ElectronsUserEmbedded_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"

//#include "EgammaAnalysis/ElectronTools/interface/EGammaMvaEleEstimator.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/TransientTrack/plugins/TransientTrackBuilderESProducer.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/Scalers/interface/DcsStatus.h"
#include "RecoEgamma/EgammaTools/interface/ConversionFinder.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "DataFormats/GeometryVector/interface/VectorUtil.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHit.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"
#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

using namespace edm;
using namespace std;
using namespace reco;

class ElectronsUserEmbedded : public edm::EDProducer{


public: 

  explicit ElectronsUserEmbedded(const edm::ParameterSet&);
  virtual ~ElectronsUserEmbedded() {};

private:

  virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup);
  //declare token
  edm::EDGetTokenT<pat::ElectronCollection> eleToken_;
  edm::EDGetTokenT<double> rhoToken_;
  edm::EDGetTokenT<reco::VertexCollection> vertexToken_;
  edm::EDGetTokenT<reco::ConversionCollection> convToken_;
  edm::EDGetTokenT<reco::BeamSpot> beamSpotToken_;
  //bool isMC_;
};

#endif

ElectronsUserEmbedded::ElectronsUserEmbedded(const edm::ParameterSet & iConfig){
  edm::ConsumesCollector&& cc = consumesCollector();
  //define token
  eleToken_ = cc.consumes<pat::ElectronCollection>(iConfig.getParameter<edm::InputTag>("electronTag"));
  vertexToken_   = cc.consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertexTag"));
  rhoToken_ = cc.consumes<double>(iConfig.getParameter<edm::InputTag>("rho"));
  beamSpotToken_ = cc.consumes<reco::BeamSpot>(iConfig.getParameter<edm::InputTag>("beamSpot"));
  convToken_ = cc.consumes<reco::ConversionCollection>(iConfig.getParameter<edm::InputTag>("conversionsMiniAOD"));
  produces<pat::ElectronCollection>("");
}

void ElectronsUserEmbedded::produce(edm::Event & iEvent, const edm::EventSetup & iSetup){

  //get electrons
  edm::Handle<pat::ElectronCollection>electronsHandle;
  iEvent.getByToken(eleToken_, electronsHandle); 
  const pat::ElectronCollection* electrons = electronsHandle.product();
  /* 
  //get vertices
  edm::Handle<reco::VertexCollection> vertexHandle;
  iEvent.getByToken(vertexToken_,vertexHandle);
  const reco::VertexCollection* vertexes = vertexHandle.product();
  */
  //Compute the rho, for relCombPFIsoEAcorr
  edm::Handle<double> hRho;
  iEvent.getByToken(rhoToken_, hRho);
  double rho_ = hRho.isValid() ? *hRho : 0;
  
  //Get the conversion collection
  edm::Handle<reco::ConversionCollection> hConversions;
  iEvent.getByToken(convToken_, hConversions);
  
  //Get the beam spot
  edm::Handle<reco::BeamSpot> bsHandle;
  iEvent.getByToken(beamSpotToken_,bsHandle);
  const reco::BeamSpot &thebs = *bsHandle.product();

  std::auto_ptr< pat::ElectronCollection > electronsUserEmbeddedColl( new pat::ElectronCollection() ) ;
  for(size_t iEle = 0; iEle < electrons->size(); iEle++){
    pat::Electron aElectron( (*electrons)[iEle] );
    float dPhi  = aElectron.deltaPhiSuperClusterTrackAtVtx();
    float dEta  = aElectron.deltaEtaSuperClusterTrackAtVtx();
    float sihih = aElectron.sigmaIetaIeta();
    float HoE   = aElectron.hadronicOverEm();

    cout<<"phi = "<<dPhi<<endl;
    cout<<"eta =  = "<<dEta<<endl;
    cout<<"HoE =  = "<<HoE<<endl;
    
    cout<<"AAAAA2"<<endl;
    //aElectron.addUserFloat("nHits",nHits);
    aElectron.addUserFloat("dPhi",fabs(dPhi));
    aElectron.addUserFloat("dEta",fabs(dEta));
    aElectron.addUserFloat("sihih",sihih);
    aElectron.addUserFloat("HoE",HoE);
    int passConvVeto = int(!ConversionTools::hasMatchedConversion(aElectron, hConversions, thebs.position()));
    aElectron.addUserInt("antiConv",passConvVeto);
    
    double dxyWrtPV =  -99.;
    double dzWrtPV  =  -99.;
    /*
    cout<<"AAAAA3"<<endl;
    if(vertexes->size()!=0 && (aElectron.gsfTrack()).isNonnull() ){
      dxyWrtPV = (aElectron.gsfTrack())->dxy( (*vertexes)[0].position() ) ;
      dzWrtPV  = (aElectron.gsfTrack())->dz(  (*vertexes)[0].position() ) ;
    }
    else if (vertexes->size()!=0 && (aElectron.track()).isNonnull() ){
      dxyWrtPV = (aElectron.track())->dxy( (*vertexes)[0].position() ) ;
      dzWrtPV  = (aElectron.track())->dz(  (*vertexes)[0].position() ) ;
    }
    */
    cout<<"AAAAA4"<<endl;
    aElectron.addUserFloat("dxyWrtPV",dxyWrtPV);
    aElectron.addUserFloat("dzWrtPV",dzWrtPV);
    
    aElectron.addUserFloat("mvaIdTrig"   ,aElectron.electronID("mvaTrigV0"));
    aElectron.addUserFloat("mvaIdNonTrig",aElectron.electronID("mvaNonTrigV0"));
    aElectron.addUserFloat("mvaIdTrigNoIP",aElectron.electronID("mvaTrigNoIPV0"));

    //isolation with custom configuration
    /*
    double EffArea_ = ElectronEffectiveArea::GetElectronEffectiveArea(ElectronEffectiveArea::kEleGammaAndNeutralHadronIso04, aElectron.superCluster()->eta(),ElectronEffectiveArea::kEleEAData2012);
    double pfRelIso04 = (aElectron.userIsolation(pat::PfChargedHadronIso) + std::max(0., ((aElectron.userIsolation(pat::PfGammaIso)+aElectron.userIsolation(pat::PfNeutralHadronIso))-(rho_*EffArea_))))/aElectron.pt();
    
    aElectron.addUserFloat("PFRelIso04", pfRelIso04);
    */
    electronsUserEmbeddedColl->push_back(aElectron);
    cout<<"AAAAA5"<<endl;
  }    

  iEvent.put( electronsUserEmbeddedColl );
  return;
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(ElectronsUserEmbedded);
