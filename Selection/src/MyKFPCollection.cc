#include "MiniTree/Selection/interface/MyEventSelection.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

std::vector<MyKineFitParticle> MyEventSelection::getKineFitParticles(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  std::vector<MyKineFitParticle> selKFParticles; 
  selKFParticles.clear();
  
  try{
    //config parameters
    std::vector<edm::InputTag> sources = configParamsKFPs_.getParameter<std::vector<edm::InputTag> >("sources");

    edm::Handle<vector<double> >chi2_;
    edm::Handle<vector<int> >status_;
    edm::Handle<vector<double> >prob_;
    edm::Handle<int> njets_;
    edm::Handle<vector<double> >chi2Up_; 
    edm::Handle<vector<int> >statusUp_; 
    edm::Handle<vector<double> >probUp_; 
    edm::Handle<int> njetsUp_; 
    edm::Handle<vector<double> >chi2Down_;  
    edm::Handle<vector<int> >statusDown_;  
    edm::Handle<vector<double> >probDown_;  
    edm::Handle<int> njetsDown_;  
    edm::Handle<vector<double> >chi2JerUp_;  
    edm::Handle<vector<int> >statusJerUp_;  
    edm::Handle<vector<double> >probJerUp_;  
    edm::Handle<int> njetsJerUp_;  
    edm::Handle<vector<double> >chi2JerDown_;   
    edm::Handle<vector<int> >statusJerDown_;   
    edm::Handle<vector<double> >probJerDown_;   
    edm::Handle<int> njetsJerDown_;
    
    try{
      iEvent.getByToken(chi2OfFitSource, chi2_);
      iEvent.getByToken(statusOfFitSource, status_);
      iEvent.getByToken(probOfFitSource, prob_);
      iEvent.getByToken(njetsOfFitSource, njets_);
    }catch(std::exception &e){
      std::cout<<" KineFitter product is not available"<<std::endl;
    }

    try{ 
      iEvent.getByToken(chi2OfFitUpSource, chi2Up_);
      iEvent.getByToken(statusOfFitUpSource, statusUp_);
      iEvent.getByToken(probOfFitUpSource, probUp_);
      iEvent.getByToken(njetsOfFitUpSource, njetsUp_);
    }catch(std::exception &e){ 
      std::cout<<" KineFitter product for JES Up is not available"<<std::endl; 
    } 
    
    try{  
      iEvent.getByToken(chi2OfFitDownSource, chi2Down_);
      iEvent.getByToken(statusOfFitDownSource, statusDown_);
      iEvent.getByToken(probOfFitDownSource, probDown_);
      iEvent.getByToken(njetsOfFitDownSource, njetsDown_);
    }catch(std::exception &e){  
      std::cout<<" KineFitter product for JES Down is not available"<<std::endl;  
    }  
    try{  
      iEvent.getByToken(chi2OfFitJERUpSource, chi2JerUp_);
      iEvent.getByToken(statusOfFitJERUpSource, statusJerUp_);
      iEvent.getByToken(probOfFitJERUpSource, probJerUp_);
      iEvent.getByToken(njetsOfFitJERUpSource, njetsJerUp_);
    }catch(std::exception &e){  
      std::cout<<" KineFitter product for JER Up is not available"<<std::endl;  
    }

    try{   
      iEvent.getByToken(chi2OfFitJERDownSource, chi2JerDown_);
      iEvent.getByToken(statusOfFitJERDownSource, statusJerDown_);
      iEvent.getByToken(probOfFitJERDownSource, probJerDown_);
      iEvent.getByToken(njetsOfFitJERDownSource, njetsJerDown_);
    }catch(std::exception &e){   
      std::cout<<" KineFitter product for JER Down is not available"<<std::endl;   
    }
    for(std::vector<edm::InputTag>::iterator sit = sources.begin(); sit != sources.end(); sit++){
      TString rawtag=sit->instance();
      std::string tag(rawtag);
      TString label = sit->label();
      std::string moduleLabel(label);
      //cout<<moduleLabel<<":"<<tag<<endl;
      edm::Handle<pat::ParticleCollection>ikfps;
      try{
        iEvent.getByLabel( *sit, ikfps);
      //cout<<"Number of KinFit Particles = "<< ikfps->size() <<endl;
      }catch(std::exception &e){
        continue;
      }
      
      if(!ikfps.isValid()) continue;
      if(ikfps->size() == 0)continue;
      for(size_t iKfp = 0; iKfp < ikfps->size(); iKfp++)
        {
          const pat::Particle jKfp = ((*ikfps)[iKfp]);
          MyKineFitParticle newKfp = MyKineFitPartConverter(jKfp, rawtag);
          newKfp.partName = tag;
          newKfp.labelName = moduleLabel;
          //cout<<moduleLabel<<endl; 
          if(moduleLabel.find("JESUp")!=std::string::npos){
            newKfp.chi2OfFit = chi2Up_->size()>0 ? (*chi2Up_)[0] : 999.; 
            newKfp.statusOfFit = statusUp_->size()>0 ? (*statusUp_)[0] : 0; 
            newKfp.probOfFit = probUp_->size() > 0 ? (*probUp_)[0] : 0; 
            newKfp.njetsOfFit = *njetsUp_;
            //std::cout<<" JES UP chi2 =  "<<newKfp.chi2OfFit<<std::endl;
          }
          
          else if(moduleLabel.find("JESDown")!=std::string::npos){ 
            newKfp.chi2OfFit = chi2Down_->size()>0 ? (*chi2Down_)[0] : 999.;  
            newKfp.statusOfFit = statusDown_->size()>0 ? (*statusDown_)[0] : 0;  
            newKfp.probOfFit = probDown_->size() > 0 ? (*probDown_)[0] : 0;  
            newKfp.njetsOfFit = *njetsDown_;
            //std::cout<<" JES Down chi2 =  "<<newKfp.chi2OfFit<<std::endl;
              }
      
          else if(moduleLabel.find("JERUp")!=std::string::npos){ 
            newKfp.chi2OfFit = chi2JerUp_->size()>0 ? (*chi2JerUp_)[0] : 999.;  
            newKfp.statusOfFit = statusJerUp_->size()>0 ? (*statusJerUp_)[0] : 0;  
            newKfp.probOfFit = probJerUp_->size() > 0 ? (*probJerUp_)[0] : 0;  
            newKfp.njetsOfFit = *njetsJerUp_;
            //std::cout<<" JER UP chi2 =  "<<newKfp.chi2OfFit<<std::endl; 
              } 
          
          else if(moduleLabel.find("JERDown")!=std::string::npos){  
            newKfp.chi2OfFit = chi2JerDown_->size()>0 ? (*chi2JerDown_)[0] : 999.;   
            newKfp.statusOfFit = statusJerDown_->size()>0 ? (*statusJerDown_)[0] : 0;   
            newKfp.probOfFit = probJerDown_->size() > 0 ? (*probJerDown_)[0] : 0;   
            newKfp.njetsOfFit = *njetsJerDown_;
            //std::cout<<" JER Down chi2 =  "<<newKfp.chi2OfFit<<std::endl; 
              }
             
          else{
            newKfp.chi2OfFit = chi2_->size()>0 ? (*chi2_)[0] : 999.;
            newKfp.statusOfFit = status_->size()>0 ? (*status_)[0] : 0;
            newKfp.probOfFit = prob_->size() > 0 ? (*prob_)[0] : 0;
            newKfp.njetsOfFit = *njets_;
            //std::cout<<" Number of jets =  "<<*njets_<<endl;
            //std::cout<<" chi2 =  "<<newKfp.chi2OfFit<<endl;
            //std::cout<<" status of fit =  "<<newKfp.statusOfFit<<endl;
            //std::cout<<" probOfFit =  "<<newKfp.probOfFit<<endl;
            //std::cout<<endl;
              }
          selKFParticles.push_back(newKfp);
        }
    fs_->cd();
  
    }
      
  }catch(std::exception &e){
    std::cout << "[KineFitParticle Collection] : check selection " << e.what() << std::endl;
  }
  
  return selKFParticles;
}
  
    
MyKineFitParticle MyEventSelection::MyKineFitPartConverter(const pat::Particle& ikfp, TString& dirtag)
{
  MyKineFitParticle newKFP;
  newKFP.Reset();
  newKFP.p4.SetCoordinates(ikfp.px(), ikfp.py(), ikfp.pz(), ikfp.energy());
  newKFP.vertex.SetCoordinates(ikfp.vx(), ikfp.vy(), ikfp.vz());
  //newKFP.part_id = ikfp.pdgId();
  //newKFP.part_id = ikfp.pid();
  //newKFP.part_mother_id = ikfp.motherID(); 
  newKFP.charge = ikfp.charge(); 
  return newKFP;
}

