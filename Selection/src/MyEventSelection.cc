#include "MiniTree/Selection/interface/MyEventSelection.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "DataFormats/JetReco/interface/JPTJet.h"

MyEventSelection::MyEventSelection(const edm::ParameterSet& iConfig, edm::ConsumesCollector&& cc)  
{
  configParamsVertex_ = iConfig.getParameter<edm::ParameterSet>("Vertex");
  configParamsJets_ = iConfig.getParameter<edm::ParameterSet>("Jets");
  configParamsMETs_ = iConfig.getParameter<edm::ParameterSet>("Mets");
  configParamsMuons_ = iConfig.getParameter<edm::ParameterSet>("Muons");
  configParamsElectrons_ = iConfig.getParameter<edm::ParameterSet>("Electrons");
  configParamshlt_ = iConfig.getParameter<edm::ParameterSet>("Trigger");
  configParamsMC_ = iConfig.getParameter<edm::ParameterSet>("MCTruth");
  configParamsKFPs_ = iConfig.getParameter<edm::ParameterSet>("KineFit");
  runKineFitter_ = configParamsKFPs_.getParameter<bool>("runKineFitter");
  
  //KFP
  //std::vector<edm::InputTag> sources = configParamsKFPs_.getParameter<std::vector<edm::InputTag> >("sources");
  edm::InputTag chi2OfFit = configParamsKFPs_.getParameter<edm::InputTag>("chi2OfFit");
  edm::InputTag statusOfFit = configParamsKFPs_.getParameter<edm::InputTag>("statusOfFit");
  edm::InputTag probOfFit = configParamsKFPs_.getParameter<edm::InputTag>("probOfFit");
  edm::InputTag njetsOfFit = configParamsKFPs_.getParameter<edm::InputTag>("njetsUsed");
  edm::InputTag chi2OfFitUp = configParamsKFPs_.getParameter<edm::InputTag>("chi2OfFitUp"); 
  edm::InputTag statusOfFitUp = configParamsKFPs_.getParameter<edm::InputTag>("statusOfFitUp"); 
  edm::InputTag probOfFitUp = configParamsKFPs_.getParameter<edm::InputTag>("probOfFitUp"); 
  edm::InputTag njetsOfFitUp = configParamsKFPs_.getParameter<edm::InputTag>("njetsUsedUp"); 
  edm::InputTag chi2OfFitDown = configParamsKFPs_.getParameter<edm::InputTag>("chi2OfFitDown");  
  edm::InputTag statusOfFitDown = configParamsKFPs_.getParameter<edm::InputTag>("statusOfFitDown");  
  edm::InputTag probOfFitDown = configParamsKFPs_.getParameter<edm::InputTag>("probOfFitDown");  
  edm::InputTag njetsOfFitDown = configParamsKFPs_.getParameter<edm::InputTag>("njetsUsedDown");  
  edm::InputTag chi2OfFitJERUp = configParamsKFPs_.getParameter<edm::InputTag>("chi2OfFitJERUp");  
  edm::InputTag statusOfFitJERUp = configParamsKFPs_.getParameter<edm::InputTag>("statusOfFitJERUp");  
  edm::InputTag probOfFitJERUp = configParamsKFPs_.getParameter<edm::InputTag>("probOfFitJERUp");  
  edm::InputTag njetsOfFitJERUp = configParamsKFPs_.getParameter<edm::InputTag>("njetsUsedJERUp");  
  edm::InputTag chi2OfFitJERDown = configParamsKFPs_.getParameter<edm::InputTag>("chi2OfFitJERDown");   
  edm::InputTag statusOfFitJERDown = configParamsKFPs_.getParameter<edm::InputTag>("statusOfFitJERDown");   
  edm::InputTag probOfFitJERDown = configParamsKFPs_.getParameter<edm::InputTag>("probOfFitJERDown");   
  edm::InputTag njetsOfFitJERDown = configParamsKFPs_.getParameter<edm::InputTag>("njetsUsedJERDown");  

  //ikfpSource = cc.consumes<pat::ParticleCollection>(sources); 
  chi2OfFitSource = cc.consumes<vector<double>>(chi2OfFit); 
  statusOfFitSource = cc.consumes<vector<int>>(statusOfFit); 
  probOfFitSource = cc.consumes<vector<double>>(probOfFit); 
  njetsOfFitSource = cc.consumes<int>(njetsOfFit); 
  chi2OfFitUpSource = cc.consumes<vector<double>>(chi2OfFitUp); 
  statusOfFitUpSource = cc.consumes<vector<int>>(statusOfFitUp); 
  probOfFitUpSource = cc.consumes<vector<double>>(probOfFitUp); 
  njetsOfFitUpSource = cc.consumes<int>(njetsOfFitUp); 
  chi2OfFitDownSource = cc.consumes<vector<double>>(chi2OfFitDown); 
  statusOfFitDownSource = cc.consumes<vector<int>>(statusOfFitDown); 
  probOfFitDownSource = cc.consumes<vector<double>>(probOfFitDown); 
  njetsOfFitDownSource = cc.consumes<int>(njetsOfFitDown); 
  chi2OfFitJERUpSource = cc.consumes<vector<double>>(chi2OfFitJERUp); 
  statusOfFitJERUpSource = cc.consumes<vector<int>>(statusOfFitJERUp); 
  probOfFitJERUpSource = cc.consumes<vector<double>>(probOfFitJERUp); 
  njetsOfFitJERUpSource = cc.consumes<int>(njetsOfFitJERUp); 
  chi2OfFitJERDownSource = cc.consumes<vector<double>>(chi2OfFitJERDown); 
  statusOfFitJERDownSource = cc.consumes<vector<int>>(statusOfFitJERDown); 
  probOfFitJERDownSource = cc.consumes<vector<double>>(probOfFitJERDown); 
  njetsOfFitJERDownSource = cc.consumes<int>(njetsOfFitJERDown); 
  
  // vertex
  vtxSource = cc.consumes<reco::VertexCollection>(configParamsVertex_.getParameter<edm::InputTag>("vertexSource"));
  bsSource = cc.consumes<reco::BeamSpot>(configParamsVertex_.getParameter<edm::InputTag>("beamSpotSource"));

  // Muon
  Muonsources = cc.consumes<pat::MuonCollection>(configParamsMuons_.getParameter<edm::InputTag>("sources")); 
  TrigEvent_ = cc.consumes<pat::TriggerEvent>(configParamsJets_.getParameter<edm::InputTag>("triggerEvent"));

  // Elctrons
  Elesources = cc.consumes<pat::ElectronCollection>(configParamsElectrons_.getParameter<edm::InputTag>("sources"));
  //EleConversion_ = cc.consumes<reco::ConversionCollection>(edm::InputTag("reducedEgamma"));
  //eventrhoToken_ = cc.consumes<double>(edm::InputTag("kt6PFJets", "rho"));
  jetIDMapToken_ = cc.consumes<reco::JetIDValueMap>(edm::InputTag("ak5JetID"));

  // Jets
  Jetsources = cc.consumes<pat::JetCollection>(configParamsJets_.getParameter<edm::InputTag>("sources"));
  //TrigEvent_ = cc.consumes<pat::TriggerObjectStandAloneCollection>(configParamsJets_.getParameter<edm::InputTag>("triggerEvent"));

  // Mets
  Metsources = cc.consumes<pat::METCollection>(configParamsMETs_.getParameter<edm::InputTag>("sources"));

  // Trigger
  hlt_ = cc.consumes<edm::TriggerResults>(configParamshlt_.getParameter<edm::InputTag>("source"));

  // MC and PU
  PUInfoTag_ = cc.consumes<vector<PileupSummaryInfo> >(edm::InputTag("slimmedAddPileupInfo"));
  GenParticle_ = cc.consumes<reco::GenParticleCollection>(edm::InputTag("prunedGenParticles"));

  std::string code = configParamsMC_.getParameter<std::string>("sampleCode");
  inputch = configParamsMC_.getParameter<std::string>("sampleChannel");
  if(code!=std::string("DATA")) { isData_=false; }
  else{ isData_=true; inputDataSampleCode_ = MyEvent::DATA; }

  if(code==std::string("TTBAR")){ inputDataSampleCode_ = MyEvent::TTBAR;  }
  if(code==std::string("ZJETS")){ inputDataSampleCode_ = MyEvent::ZJETS;  }
  if(code==std::string("WJETS")){ inputDataSampleCode_ = MyEvent::WJETS;  }
  if(code==std::string("TOPS")) { inputDataSampleCode_ = MyEvent::TOPS;   }
  if(code==std::string("TBARS")) { inputDataSampleCode_ = MyEvent::TBARS; }
  if(code==std::string("TOPT")) { inputDataSampleCode_ = MyEvent::TOPT;   }
  if(code==std::string("TBART")) { inputDataSampleCode_ = MyEvent::TBART; }
  if(code==std::string("TOPW")) { inputDataSampleCode_ = MyEvent::TOPW;   }
  if(code==std::string("TBARW")) { inputDataSampleCode_ = MyEvent::TBARW; }
  if(code==std::string("QCD" )) { inputDataSampleCode_ = MyEvent::QCD;    }
  if(code==std::string("QCD2030")) {inputDataSampleCode_ = MyEvent::QCD2030;}
  if(code==std::string("QCD3080")) {inputDataSampleCode_ = MyEvent::QCD3080;}
  if(code==std::string("QCD80170")) {inputDataSampleCode_ = MyEvent::QCD80170;}
  if(code==std::string("QCD170250")) {inputDataSampleCode_ = MyEvent::QCD170250;}
  if(code==std::string("WH")) { inputDataSampleCode_ = MyEvent::WH; }
  if(code==std::string("HH")) { inputDataSampleCode_ = MyEvent::HH; }
  if(code==std::string("")) { inputDataSampleCode_ = MyEvent::OTHER; }
  if(code==std::string("W1JETS")) { inputDataSampleCode_ = MyEvent::W1JETS; }
  if(code==std::string("W2JETS")) { inputDataSampleCode_ = MyEvent::W2JETS; }
  if(code==std::string("W3JETS")) { inputDataSampleCode_ = MyEvent::W3JETS; }
  if(code==std::string("W4JETS")) { inputDataSampleCode_ = MyEvent::W4JETS; }
  if(code==std::string("Z1JETS")) { inputDataSampleCode_ = MyEvent::Z1JETS; }
  if(code==std::string("Z2JETS")) { inputDataSampleCode_ = MyEvent::Z2JETS; }
  if(code==std::string("Z3JETS")) { inputDataSampleCode_ = MyEvent::Z3JETS; }
  if(code==std::string("Z4JETS")) { inputDataSampleCode_ = MyEvent::Z4JETS; }
  if(code==std::string("WW"))   { inputDataSampleCode_ = MyEvent::WW;     }
  if(code==std::string("WZ"))   { inputDataSampleCode_ = MyEvent::WZ;     }
  if(code==std::string("ZZ"))   { inputDataSampleCode_ = MyEvent::ZZ;     }
}

MyEventSelection::~MyEventSelection()
{

}

void MyEventSelection::Set(const edm::Event& e, const edm::EventSetup& es)
{

  es.get<TransientTrackRecord>().get("TransientTrackBuilder", trackBuilder);
  event_.eventNb = e.id().event();
  event_.lumiblock = e.luminosityBlock();
  event_.isData = isData_;
  
  //get trigger, vertex, muon, electron, jet, met
  event_.hlt = getHLT(e, es);
  event_.PrimaryVtxs = getVertices(e, es);
  event_.Muons = getMuons(e, es);
  event_.Electrons = getElectrons(e, es);
  event_.Jets = getJets(e, es);
  event_.mets = getMETs(e, es);
  //std::cout<<"pass met "<<event_.mets.size()<<std::endl;
  
  if(!isData_){
    event_.mcParticles = getMCParticles(e);
    event_.mcMET = mcMET;
    event_.sampleInfo = getSampleInfo(e, es);
  }
  //store kinefit information
  if(runKineFitter_)event_.KineFitParticles = getKineFitParticles(e, es);

  //make event selection
  bool passTrig = false;
  std::vector<std::string> trigs = event_.hlt;
  for(size_t itrig = 0; itrig < trigs.size(); itrig++){
    if(trigs[itrig].find("Ele") != std::string::npos){passTrig = true; cout <<"ele trig passed"<<endl;}
    if(trigs[itrig].find("Mu") != std::string::npos){passTrig = true; cout<<"mu trig passed"<<endl;}
  }
  int nIsoMuon = 0, nIsoElectron = 0;
  std::vector<MyElectron> electrons = event_.Electrons;
  for(size_t iele = 0; iele < electrons.size(); iele++){
    //std::string algo = electrons[iele].eleName;
    std::string algo(electrons[iele].eleName);
    //if(algo.find("PFlow") == std::string::npos) continue;
    bool passKin = false, passId = false, passIso = false;
    int quality = electrons[iele].quality;
    if(quality & 0x1)passKin = true;
    if((quality >> 1) & 0x1)passId = true;
    if((quality >> 2) & 0x1)passIso = true;
    if(passKin && passId && passIso){
    ///if(passKin && passId){
     myhistos_["SelElePt"]->Fill(electrons[iele].p4.Pt());
     myhistos_["SelEleEta"]->Fill(electrons[iele].p4.Eta());
      nIsoElectron++;
    }
  }
  myhistos_["SelEleMultiplicity"]->Fill(nIsoElectron);
  std::vector<MyMuon> muons = event_.Muons;
  for(size_t imu = 0; imu < muons.size(); imu++){
    //std::string algo = muons[imu].muName;
    std::string algo(muons[imu].muName);
    //if(algo.find("PFlow") == std::string::npos) continue;
    bool passKin = false, passId = false;///, passIso = false;
    int quality = muons[imu].quality;
    if(quality & 0x1)passKin = true;
    if((quality >> 1) & 0x1)passId = true;
    ///if((quality >> 2) & 0x1)passIso = true;
    ///if(passKin && passId && passIso){
    if(passKin && passId){
      myhistos_["SelMuPt"]->Fill(muons[imu].p4.Pt());
      myhistos_["SelMuEta"]->Fill(muons[imu].p4.Eta());
      nIsoMuon++;
    }
  }
  myhistos_["SelMuMultiplicity"]->Fill(nIsoMuon);

  int nIsoLepton = 0;
  //  int nIsoLepton = nIsoMuon + nIsoElectron;
  if(inputch==std::string("electron")){ nIsoLepton = nIsoElectron;/* std::cout << "elctron found" << std::endl;*/}
  //  int nIsoLepton = nIsoElectron;
  if(inputch==std::string("muon")){ nIsoLepton = nIsoMuon; /*std::cout << "muon found" << std::endl;*/}

  std::vector<MyJet> jets = event_.Jets;
  int nJets = 0, nHighPtJets = 0;
  for(size_t ijet = 0; ijet < jets.size(); ijet++){
    //std::string algo = jets[ijet].jetName;
    std::string algo(jets[ijet].jetName);
    //if(algo.find("PFlow") == std::string::npos) continue;
    if(isData_ && algo.find("ResCor") == std::string::npos) continue;
    ///if(isData_ && algo.find("ResCor") == std::string::npos) continue;
    bool passKin = false, passId = false;
    int quality = jets[ijet].quality;
    if(quality & 0x1)passKin = true;
    if((quality >> 1) & 0x1)passId = true;
    if(passKin && passId){
      myhistos_["SelJetPt"]->Fill(jets[ijet].p4.Pt());
      myhistos_["SelJetEta"]->Fill(jets[ijet].p4.Eta());
      nJets++;
      if(jets[ijet].p4.Pt() > 30)nHighPtJets++;
    }
  }
  myhistos_["SelJetMultiplicity"]->Fill(nJets);

  int EventQuality = 0;
  if(passTrig){
    EventQuality++;
    if(nIsoLepton > 0){
      EventQuality++;
      if(nJets > 2){
	EventQuality++;
	if(nHighPtJets > 0){
	  EventQuality++;
	  if(nHighPtJets > 1){
	    EventQuality++;
	  }
	}
      }
    }
  }

  for(int istep = 0; istep <= EventQuality; istep++){
    myhistos_["cutflow"]->Fill(istep);
  }

  event_.eventQuality = EventQuality;
  fs_->cd();
}


//void MyEventSelection::BookHistos(edm::Service<TFileService> tfs_)
void MyEventSelection::BookHistos()
{
  ///book histograms
  initTriggerHistos_ = true;
  
  ///selection
  dirs_.push_back( fs_->mkdir("selection") );
  myhistos_["cutflow"] = dirs_[dirs_.size() - 1].make<TH1D>("cutflow", "cutflow", 10, 0., 10.);
  myhistos2_["cutflowmctruth"] = dirs_[dirs_.size() - 1].make<TH2D>("cutflowmctruth", "cutflow", 10, 0., 10., 18, 0., 18.);
  TString steps[6] = {"reco","trigger","#geq 1 leptons","#geq 1 jet","#geq 1 jet (pT > 25)", "#geq 2 jets (pT > 25)"};
  TString ttch[18] = {"unk.", "full had","e+jets","#mu+jets","#tau+jets","ee","e#mu","e#tau","#mu#mu","#mu#tau","#tau#tau", "z+jets","z#tau#tau","w+jets","top-s", "top-t", "top-w","qcd"};
  const size_t nsteps = sizeof(steps)/sizeof(TString);
  for(uint istep=0; istep<nsteps; istep++ ){
    myhistos2_["cutflowmctruth"]->GetXaxis()->SetBinLabel(istep+1, steps[istep]);
    myhistos_["cutflow"]->GetXaxis()->SetBinLabel(istep+1, steps[istep]);
  }
  for(int ich=0;   ich<18;  ich++  ){
    myhistos2_["cutflowmctruth"]->GetYaxis()->SetBinLabel(ich+1, ttch[ich]);
  }

  myhistos_["SelJetPt"]  = dirs_[dirs_.size() - 1].make<TH1D>("SelJetPt", "jet Pt",200, 0, 400.);
  myhistos_["SelJetEta"]  = dirs_[dirs_.size() - 1].make<TH1D>("SelJetEta", "jet Eta;jet #eta;N_{events}",100, -5.0, 5.0);
  myhistos_["SelJetMultiplicity"]  = dirs_[dirs_.size() - 1].make<TH1D>("SelJetMultiplicity", "jet Multi",20, 0, 20);
  myhistos_["SelElePt"]  = dirs_[dirs_.size() - 1].make<TH1D>("SelElePt", "electron Pt",200, 0, 400.);
  myhistos_["SelEleEta"]  = dirs_[dirs_.size() - 1].make<TH1D>("SelEleEta", "ele Eta",100, -5.0, 5.0);
  myhistos_["SelEleMultiplicity"]  = dirs_[dirs_.size() - 1].make<TH1D>("SelEleMultiplicity", "electron Multi",20, 0, 20);
  myhistos_["SelMuPt"]  = dirs_[dirs_.size() - 1].make<TH1D>("SelMuPt", "muon Pt",200, 0, 400.);
  myhistos_["SelMuEta"]  = dirs_[dirs_.size() - 1].make<TH1D>("SelMuEta", "muon Eta;" ,100, -5.0, 5.0);
  myhistos_["SelMuMultiplicity"]  = dirs_[dirs_.size() - 1].make<TH1D>("SelMuMultiplicity", "muon Multi;",20, 0, 20);

  ///MC
  dirs_.push_back( fs_->mkdir("MCINFO") );
  myhistos_["intimepu"] = dirs_[dirs_.size() - 1].make<TH1D>("intimepu", "intime pileup", 101, -0.5, 100.5);
  myhistos_["outoftimepu"] = dirs_[dirs_.size() - 1].make<TH1D>("outoftimepu", "out of time pileup", 101, -0.5, 100.5);
  myhistos_["totalpu"] = dirs_[dirs_.size() - 1].make<TH1D>("totalpu", "total pileup", 101, -0.5, 100.5);
  myhistos_["trueintimepu"] = dirs_[dirs_.size() - 1].make<TH1D>("trueintimepu", "intime pileup", 600, 0., 60.); 
  myhistos_["trueoutoftimepu"] = dirs_[dirs_.size() - 1].make<TH1D>("trueoutoftimepu", "out of time pileup",600,0.,60.); 
  myhistos_["truetotalpu"] = dirs_[dirs_.size() - 1].make<TH1D>("truetotalpu", "total pileup", 600, 0., 60.);

  ///Jets
  TString jetrawtag="Jets";
  std::string jettag(jetrawtag);
  //Make a new TDirectory
  dirs_.push_back( fs_->mkdir(jettag.c_str()) );
  myhistos_["pt_"+jetrawtag] = dirs_[dirs_.size() - 1].make<TH1D>("pt_"+jetrawtag, "Jet Pt", 200, 0., 500.);
  myhistos_["eta_"+jetrawtag] = dirs_[dirs_.size() - 1].make<TH1D>("eta_"+jetrawtag, "Jet #eta", 100, -5.0, 5.0);
  myhistos_["phi_"+jetrawtag] = dirs_[dirs_.size() - 1].make<TH1D>("phi_"+jetrawtag, "Jet #phi", 80, -4.05, 3.95);
  myhistos_["emf_"+jetrawtag] = dirs_[dirs_.size() - 1].make<TH1D>("emf_"+jetrawtag, "Jet emf", 120, 0, 1.02);

  ///Electrons
  TString elerawtag="Electrons";
  std::string eletag(elerawtag);
  //Make a new TDirectory
  dirs_.push_back( fs_->mkdir(eletag.c_str()) );
  myhistos_["pt_"+elerawtag] = dirs_[dirs_.size() - 1].make<TH1D>("pt_"+elerawtag, "Electron Pt", 200, 0., 500.);
  myhistos_["eta_"+elerawtag] = dirs_[dirs_.size() - 1].make<TH1D>("eta_"+elerawtag, "Electron #eta", 60, -3.0, 3.0);
  myhistos_["phi_"+elerawtag] = dirs_[dirs_.size() - 1].make<TH1D>("phi_"+elerawtag, "Electron #phi", 80, -4.05, 3.95);
  myhistos_["pfRelIso_"+elerawtag] = dirs_[dirs_.size() - 1].make<TH1D>("pfRelIso_"+elerawtag, "Electron rel pf iso", 100, 0, 5.);

  ///Muons
  TString murawtag="Muons";
  std::string mutag(murawtag);
  //Make a new TDirectory
  dirs_.push_back( fs_->mkdir(mutag.c_str()) );	  
  myhistos_["pt_"+murawtag] = dirs_[dirs_.size() - 1].make<TH1D>("pt_"+murawtag, "Muon Pt", 200, 0., 500.);
  myhistos_["eta_"+murawtag] = dirs_[dirs_.size() - 1].make<TH1D>("eta_"+murawtag, "Muon #eta", 60, -3.0, 3.0);
  myhistos_["phi_"+murawtag] = dirs_[dirs_.size() - 1].make<TH1D>("phi_"+murawtag, "Muon #phi", 80, -4.05, 3.95);
  
  myhistos_["normChi2_"+murawtag] = dirs_[dirs_.size() - 1].make<TH1D>("normChi2_"+murawtag, "Muon track norm Chi2/dof", 200, 0, 40.);
  myhistos_["nHits_"+murawtag] = dirs_[dirs_.size() - 1].make<TH1D>("nHits_"+murawtag, "Muon track Hits", 50, 0, 50.);
  myhistos_["nMuonHits_"+murawtag] = dirs_[dirs_.size() - 1].make<TH1D>("nMuonHits_"+murawtag, "Muon track muon Hits", 50, 0, 50.);
  myhistos_["D0_"+murawtag] = dirs_[dirs_.size() - 1].make<TH1D>("D0_"+murawtag, "Muon D0", 100, 0, 500.);
  myhistos_["Dz_"+murawtag] = dirs_[dirs_.size() - 1].make<TH1D>("Dz_"+murawtag, "Muon Dz", 100, 0, 500.);
  myhistos_["pfRelIso_"+murawtag] = dirs_[dirs_.size() - 1].make<TH1D>("pfRelIso_"+murawtag, "Muon pf reliso", 100, 0, 5.); 

  ///METs
  TString metrawtag="METs";
  std::string mettag(metrawtag);
  //Make a new TDirectory
  dirs_.push_back( fs_->mkdir(mettag.c_str()) );
  myhistos_["pt_"+metrawtag] = dirs_[dirs_.size() - 1].make<TH1D>("met_"+metrawtag, "MET", 200, 0., 500.);
  myhistos_["sumet_"+metrawtag] = dirs_[dirs_.size() - 1].make<TH1D>("sumet_"+metrawtag, "sum Et", 200, 0., 500.);
  myhistos_["phi_"+metrawtag] = dirs_[dirs_.size() - 1].make<TH1D>("phi_"+metrawtag, "MET", 80, -4.05, 3.95);
}
