// -*- C++ -*-
//
// Original Author:  Aruna Kumar Nayak
//         Created:  Fri Mar 11 12:42:51 WET 2011
// $Id: MyEventSelection.h,v 1.4 2012/10/15 13:17:24 anayak Exp $
//
//

#ifndef __MYEVENTSELECTION_H__
#define __MYEVENTSELECTION_H__


// system include files
#include <memory>
#include <string>

// user include files
#include <TROOT.h>
#include <vector>
#include <TString.h>

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "DataFormats/TrackReco/interface/DeDxData.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHit.h"

#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"
#include "PhysicsTools/SelectorUtils/interface/JetIDSelectionFunctor.h"
#include "PhysicsTools/SelectorUtils/interface/strbitset.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/MET.h"
//#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Particle.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"

#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

//---------------- 13 TeV -------
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"
#include "PhysicsTools/SelectorUtils/interface/CutApplicatorWithEventContentBase.h"
#include "PhysicsTools/SelectorUtils/interface/CutApplicatorBase.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "MyEvent.h"

#include "TH1.h"
#include "TH2.h"
#include "TString.h"
#include <vector>

using namespace std;

//namespace edm {
//  class ConsumesCollector;
//}

class MyEventSelection
{
public:
  MyEventSelection(const edm::ParameterSet&, edm::ConsumesCollector&& );
  ~MyEventSelection();
  
  //void Print(std::ostream &os = std::cout) const;
  void Set(const edm::Event& e, const edm::EventSetup& es);
  void Reset() {event_.Reset();}
  MyEvent * getData() {return &event_;}
  
  
  //user functions
  std::vector<std::string> getHLT(const edm::Event&, const edm::EventSetup&);
  std::vector<MyVertex> getVertices(const edm::Event&, const edm::EventSetup&);
  MyVertex MyVertexConverter(const reco::Vertex&);
  std::vector<MyJet> getJets(const edm::Event&, const edm::EventSetup&);
  MyJet MyJetConverter(const pat::Jet&, TString&);
  std::vector<MyMET> getMETs(const edm::Event&, const edm::EventSetup&);
  MyMET MyMETConverter(const pat::MET&, TString&);
  std::vector<MyElectron> getElectrons(const edm::Event&, const edm::EventSetup&);
  MyElectron MyElectronConverter(const pat::Electron&, TString&);
  std::vector<MyMuon> getMuons(const edm::Event&, const edm::EventSetup&);
  MyMuon MyMuonConverter(const pat::Muon&, TString&);
//  std::vector<MyTau> getTaus(const edm::Event&, const edm::EventSetup&);
//  MyTau MyTauConverter(const pat::Tau&, TString&);
  std::vector<MyKineFitParticle> getKineFitParticles (const edm::Event&, const edm::EventSetup&);
  MyKineFitParticle MyKineFitPartConverter(const pat::Particle&, TString&);
  
  MyTrack myTrackConverter(const reco::TransientTrack&);
  MyTrack myTrackConverter(const reco::Track&);
  MyTrack myTrackConverter(const reco::PFCandidate&);

  std::vector<MyMCParticle> getMCParticles(const edm::Event&);
  int findMother(std::vector<MyMCParticle>,const reco::Candidate*);
  MyMET mcMET;
  SampleInfo getSampleInfo(const edm::Event&, const edm::EventSetup&);
  
  static bool sumPtOrder(const reco::Vertex *, const reco::Vertex *);
  std::vector<double> defaultMuonIsolation(const pat::Muon&, bool isPF=false);
  std::vector<double> defaultPFMuonIsolation(const pat::Muon&);
  std::vector<double> defaultElectronIsolation(const pat::Electron&, bool isPF=false);
  // ------------ 13TeV
  std::vector<double> defaultPFElectronIsolation(const pat::Electron&,bool isPF=false);

  std::vector<double> defaultPFElectronIsolation (const pat::Electron&, double);
  int assignDYchannel(const edm::Event&, const edm::EventSetup&);
  int assignWJets(const edm::Event&, const edm::EventSetup&);
  int assignTTEvent(const edm::Event&, const edm::EventSetup&);
//  pat::Tau* getTauMatchedtoJet(const pat::Jet& iJet, const std::vector<pat::Tau> *tauColl);

  // ---- General MyEventSelection information.
  //void BookHistos(edm::Service<TFileService>);
  void BookHistos();

private:
  bool fillHLT_;
  MyEvent event_;
  
  //configuration parameters
  edm::ParameterSet configParamsVertex_;
  edm::ParameterSet configParamsElectrons_;
  edm::ParameterSet configParamsMuons_;
  edm::ParameterSet configParamsJets_;
  edm::ParameterSet configParamsMETs_;
  edm::ParameterSet configParamsTaus_;
  edm::ParameterSet configParamshlt_;
  edm::ParameterSet configParamsMC_;
  edm::ParameterSet configParamsKFPs_;
  //PVx
  //  edm::Handle<reco::VertexCollection> vtxSource;
  edm::EDGetTokenT<reco::VertexCollection> vtxSource;

  edm::Handle<reco::BeamSpot> beamSpot_; // defined here as used by electron selection
  edm::EDGetTokenT<reco::BeamSpot> bsSource; // new 76x

  // Muon
  edm::EDGetTokenT<pat::MuonCollection> Muonsources; 

  // Electrons
  edm::EDGetTokenT<pat::ElectronCollection> Elesources;
  edm::EDGetTokenT<reco::ConversionCollection> EleConversion_;
  edm::EDGetTokenT<double> eventrhoToken_;

  // Jets
  edm::EDGetTokenT<pat::JetCollection> Jetsources;
  edm::EDGetTokenT<pat::TriggerEvent> TrigEvent_;
  //edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> TrigEvent_;
  edm::EDGetTokenT<reco::JetIDValueMap> jetIDMapToken_;
  // MET
  edm::EDGetTokenT<pat::METCollection> Metsources;

  // Trigger 
  edm::EDGetTokenT<edm::TriggerResults>  hlt_;

  const reco::Vertex *bestPrimVertex_;
  reco::Vertex refVertex_;
  math::XYZPoint refPoint_;

  edm::ESHandle<TransientTrackBuilder> trackBuilder;

  // MC and PU
  edm::EDGetTokenT<vector<PileupSummaryInfo>> PUInfoTag_;
  edm::EDGetTokenT<reco::GenParticleCollection> GenParticle_;

  //JET id functors
  JetIDSelectionFunctor jetIDFunctor_;
  PFJetIDSelectionFunctor pfjetIDFunctor_;
  edm::Handle<reco::JetIDValueMap> hJetIDMap;

  //electron
  //the rec hits 
  edm::Handle< EcalRecHitCollection > ebRecHits_, eeRecHits_;

  edm::Service<TFileService> fs_;
  std::vector<TFileDirectory> dirs_;
  std::map<TString, TH1D*>myhistos_;
  std::map<TString, TH2D*>myhistos2_;

  bool initTriggerHistos_;
  //is data flag
  bool isData_;
  int mcEvtType_;
  int inputDataSampleCode_;
  bool runKineFitter_; 
  std::string inputch;

  //pu re-weighting
  edm::LumiReWeighting LumiWeights_, LumiWeightsDefault_;
  //define data and MC pu vector
  std::vector< float > MCPUDist, MCPUTrueGen;
  std::vector< float > DataPUDist;

};
#endif
