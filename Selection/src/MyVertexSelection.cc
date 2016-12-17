#include "MiniTree/Selection/interface/MyEventSelection.h"

std::vector<MyVertex> MyEventSelection::getVertices(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  std::vector<MyVertex> selVertices; 
  selVertices.clear();

  try{
    bestPrimVertex_ = 0;
    refPoint_ = math::XYZPoint(0,0,0);

    //double maxZ = configParamsVertex_.getParameter<double>("maxZ");
    //double maxRho = configParamsVertex_.getParameter<double>("maxRho");
    //int minNDOF = configParamsVertex_.getParameter<int>("minNDOF");

    edm::Handle<reco::VertexCollection>vtx_;
    iEvent.getByToken(vtxSource, vtx_); // 76x
    std::vector<const reco::Vertex *> selVtx; selVtx.clear();
    for(size_t ivtx = 0; ivtx < vtx_->size(); ivtx++)
      {
	const reco::Vertex *vIt = &((*vtx_)[ivtx]);
	
	//base quantities
	//bool isReal = !(vIt->isFake());
	//double z = fabs(vIt->z());
	//double rho = vIt->position().Rho();
	//int ndof = vIt->ndof();
    //if( isReal && z < maxZ && rho < maxRho && ndof >= minNDOF )
      selVtx.push_back(vIt);
    }
    //std::sort(selVtx.begin(), selVtx.end(), &sumPtOrder);
    if(selVtx.size())bestPrimVertex_ = selVtx[0];

    //iEvent.getByToken( bsSource, beamSpot_);  // new 76x
	refPoint_ = bestPrimVertex_->position();
	refVertex_ = *bestPrimVertex_;
	//refPoint_ = beamSpot_->position();
	//const reco::BeamSpot &bs = *(beamSpot_.product());
	//reco::Vertex bsVtx( bs.position(), bs.covariance3D() );
	//refVertex_ = bsVtx;

    for(size_t ivtx = 0; ivtx < selVtx.size(); ivtx++)
      {
	const reco::Vertex *vIt = selVtx[ivtx];
	MyVertex newVertex = MyVertexConverter(*vIt);
	selVertices.push_back(newVertex);
      }
  }catch(std::exception &e){
    std::cout << "[Vertex Selection] : check selection " << e.what() << std::endl;
  }
  
  return selVertices;
}


MyVertex MyEventSelection::MyVertexConverter(const reco::Vertex& iVertex)
{
  MyVertex newVertex;
  newVertex.Reset();
  
  newVertex.chi2 = iVertex.chi2();
  newVertex.ErrXYZ.SetCoordinates(iVertex.xError(), iVertex.yError(), iVertex.zError());
  newVertex.isValid = !(iVertex.isFake());
  newVertex.ndof = iVertex.ndof();
  newVertex.normalizedChi2 = iVertex.chi2()/iVertex.ndof();
  newVertex.rho = iVertex.position().Rho();
  newVertex.XYZ.SetCoordinates(iVertex.x(), iVertex.y(), iVertex.z());

  return newVertex;
}

