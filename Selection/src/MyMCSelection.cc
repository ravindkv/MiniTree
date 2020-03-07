#include "MiniTree/Selection/interface/MyEventSelection.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"

std::vector<MyMCParticle> MyEventSelection::getMCParticles(const edm::Event& iEvent){
  std::vector<MyMCParticle> mcParticles;
  edm::Handle<reco::GenParticleCollection> genParticles;
  try{
    iEvent.getByToken(GenParticle_, genParticles); 
  }catch(...) {;}
  //----------------------------------------------
  //PDG codes of the particles:http: //pdg.lbl.gov/2007/reviews/montecarlorpp.pdf
  //http://home.thep.lu.se/~torbjorn/pythia82html/ParticleProperties.html
  //----------------------------------------------
  if(genParticles.isValid()){
    //std::cout << "MC particles size " << genParticles->size() << std::endl;
    for(size_t i = 0; i < genParticles->size(); ++ i){
	  const reco::GenParticle & part = (*genParticles)[i];
      //only for outgoing top quarks
      if(std::abs(part.pdgId())==6 && part.isLastCopy()){
	    MyMCParticle mcParticle;
        mcParticle.pid    = part.pdgId();
        mcParticle.status = part.status();
        mcParticle.isLastCopy = part.isLastCopy();
        mcParticle.p4Gen.SetCoordinates(part.px(), part.py(), part.pz(), part.energy());
        mcParticles.push_back(mcParticle);
      }
    }
  }
  //std::cout<<"stored mc particles =  "<<mcParticles.size()<<std::endl;
  return mcParticles;
}


MySampleInfo MyEventSelection::getSampleInfo(const edm::Event& iEvent, const edm::EventSetup& iSetup){
  MySampleInfo mcInfo;
  mcInfo.sampleName = configParamsMC_.getParameter<std::string>("sampleCode");
  //----------------------------------------------
  //store GenPileup info
  //----------------------------------------------
  double npuVertices_=0, nOOTpuVertices_=0;
  double nTruePuVertices_=0, nTrueOOTPuVertices_=0;
  edm::Handle<std::vector<PileupSummaryInfo> > puInfoH;
  iEvent.getByToken(PUInfoTag_, puInfoH);
 
  if(puInfoH.isValid()){ 
    //std::cout << "valid puInfoH = " << std::endl;
    double nOOTpuVertices(0),npuVertices(0);
    double nTrueOOTPuVertices(0),nTruePuVertices(0);
    for(std::vector<PileupSummaryInfo>::const_iterator it =puInfoH->begin(); it != puInfoH->end(); it++){
	  if(it->getBunchCrossing() ==0){
	    npuVertices += it->getPU_NumInteractions();
	    nTruePuVertices += it->getTrueNumInteractions();
	  }
	  else{
	    nOOTpuVertices += it->getPU_NumInteractions();
	    nTrueOOTPuVertices += it->getTrueNumInteractions();
	  }
	}
    npuVertices_ = npuVertices;
    nOOTpuVertices_ = nOOTpuVertices;
    nTruePuVertices_ = nTruePuVertices;
    nTrueOOTPuVertices_ = nTrueOOTPuVertices;
    // std::cout<<"npuVertices_ =  "<<npuVertices_<<std::endl;
  }

  std::vector<double>pu; pu.clear();
  pu.push_back(npuVertices_);
  pu.push_back(nOOTpuVertices_);

  std::vector<double>putrue; putrue.clear(); 
  putrue.push_back(nTruePuVertices_); 
  putrue.push_back(nTrueOOTPuVertices_);

  mcInfo.pileup = pu;
  mcInfo.truepileup = putrue;

  myhistos_["intimepu"]->Fill(npuVertices_);
  myhistos_["outoftimepu"]->Fill(nOOTpuVertices_);
  myhistos_["totalpu"]->Fill(npuVertices_+nOOTpuVertices_);
  myhistos_["trueintimepu"]->Fill(nTruePuVertices_); 
  myhistos_["trueoutoftimepu"]->Fill(nTrueOOTPuVertices_); 
  myhistos_["truetotalpu"]->Fill(nTruePuVertices_+nTrueOOTPuVertices_);

 
  //----------------------------------------------
  //get total number of particles (in, inter, out) 
  //in an event at gen level. It is called hepNuP
  //----------------------------------------------
  int hepNUP_ = -99;
  std::vector<int> hepIDUP_;
  std::vector<int> hepISTUP_;
  edm::Handle<LHEEventProduct > LHEHandle;
  const LHEEventProduct* LHE = 0;
  iEvent.getByToken(externalLHEProducer_, LHEHandle);
  if(LHEHandle.isValid()){
    LHE = LHEHandle.product();
    hepNUP_ = (LHE->hepeup()).NUP;
    for(size_t i=0; i<(LHE->hepeup()).IDUP.size(); i++){
      hepIDUP_.push_back((LHE->hepeup()).IDUP[i]);
      hepISTUP_.push_back((LHE->hepeup()).ISTUP[i]);
    }
  }
  mcInfo.hepNUP = hepNUP_;
  mcInfo.hepIDUP = hepIDUP_;
  mcInfo.hepISTUP = hepISTUP_;
  return mcInfo;
}
