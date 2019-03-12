#include "MiniTree/interface/MyEvent.h"
#include "MiniTree/interface/MyJet.h"
#include "MiniTree/interface/MyMET.h"
#include "MiniTree/interface/MyTrack.h"
#include "MiniTree/interface/MyVertex.h"
#include "MiniTree/interface/MyElectron.h"
#include "MiniTree/interface/MyMuon.h"
//#include "MiniTree/interface/MyTau.h"
#include "MiniTree/interface/MyMCParticle.h"
#include "MiniTree/interface/SampleInfo.h"
#include "MiniTree/interface/MomentumVec.h"
#include "MiniTree/interface/MyKineFitParticle.h"

#include<vector>
#include "TROOT.h"

namespace{
  namespace{
    std::map<int   , std::vector<int> >        dummy1;
    std::pair<float, std::string>              dummy2;
    std::vector<std::pair<float, std::string> > dummy3;
    MyEvent          Myevt; 
    MyVertex         Myvertex; 
    MyTrack          Mytrack; 
    MyJet            Myjet; 
    MyMET            Mymet; 
    MyElectron       Myele; 
    MyMuon           Mymuon; 
//    MyTau            Mytau; 
    MyMCParticle     Mymcparticle; 
    SampleInfo       sampleinfo;
    MyKineFitParticle Mykinefitparticle;
    std::vector<MyVertex>         Myvertices; 
    std::vector<MyTrack>          Mytracks; 
    std::vector<MyJet>            Myjets; 
    std::vector<MyMET>            Mymets; 
    std::vector<MyElectron>       Myeles; 
    std::vector<MyMuon>           Mymuons; 
//    std::vector<MyTau>            Mytaus; 
    std::vector<MyMCParticle>     Mymcparticles; 
    std::vector<MyKineFitParticle> Mykinefitparticles;
    std::vector<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > > lvec;
    MyLorentzVector         vec;
    Point3D               point;  
  }
}
