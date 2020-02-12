#include <algorithm>

#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "MiniTree/Selection/plugins/JetEnergyScale.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

JetEnergyScale::JetEnergyScale(const edm::ParameterSet& cfg):
  inputJets_           (cfg.getParameter<edm::InputTag>("inputJets"           )),
  inputMETs_           (cfg.getParameter<edm::InputTag>("inputMETs"           )),
  payload_             (cfg.getParameter<std::string>  ("payload"             )),  
  scaleType_           (cfg.getParameter<std::string>  ("scaleType"           )),  
  resolutionFactor_    (cfg.getParameter<std::vector<double> > ("resolutionFactors"   )),
  resolutionRanges_    (cfg.getParameter<std::vector<double> > ("resolutionEtaRanges" ))
{
  //Jets
  jetToken = consumes <pat::JetCollection> (edm::InputTag(std::string(inputJets_.label())));
  metToken = consumes <pat::METCollection> (edm::InputTag(std::string(inputMETs_.label())));
  m_rho_token  = consumes<double>(edm::InputTag(std::string("fixedGridRhoFastjetAll")));

  //jetToken = consumes <pat::JetCollection> (edm::InputTag(std::string("slimmedJets")));
  //metToken = consumes <pat::METCollection> (edm::InputTag(std::string("slimmedMETs")));

  //----------------------------------
  //define allowed types
  //----------------------------------
  allowedTypes_.push_back(std::string("jes:up"));
  allowedTypes_.push_back(std::string("jes:down"));
  allowedTypes_.push_back(std::string("jer")); //It does nothing except jer smearing

  // use label of input to create label for output
  outputJets_ = inputJets_.label();
  outputMETs_ = inputMETs_.label(); 

  // register products
  produces<std::vector<pat::Jet> >(outputJets_);
  produces<std::vector<pat::MET> >(outputMETs_); 
}
//----------------------------------
//beginJob()
//----------------------------------
void JetEnergyScale::beginJob(){ 
  // check if scaleType is ok
  if(std::find(allowedTypes_.begin(), allowedTypes_.end(), scaleType_)==allowedTypes_.end()){
    edm::LogError msg("JetEnergyScale"); 
    msg << "Unknown scaleType: " << scaleType_ << " allowed types are: \n";
    for(std::vector<std::string>::const_iterator type=allowedTypes_.begin(); type!=allowedTypes_.end(); ++type){
      msg << *type << "\n";
    }
    msg << "Please modify your configuration accordingly \n";
    throw cms::Exception("Configuration Error");
  }		
}
//----------------------------------
//Run the EDAnalyser on every event
//----------------------------------
void JetEnergyScale::produce(edm::Event& event, const edm::EventSetup& setup){
  // access jets, METs
  edm::Handle<pat::JetCollection>jets;
  event.getByToken(jetToken, jets);
  edm::Handle<pat::METCollection>mets;
  event.getByToken( metToken, mets);
  //Get relative pt resolution of jets
  //https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyResolution
  edm::Handle<double> rho;
  event.getByToken(m_rho_token, rho);
  //create two new collections for jets and MET
  std::auto_ptr<pat::JetCollection > pJets(new pat::JetCollection);
  std::auto_ptr<pat::METCollection> pMETs(new pat::METCollection);
  JME::JetResolution resolution = JME::JetResolution::get(setup, "AK4PF_pt");
  // handle to the jet corrector parameters collection
  edm::ESHandle<JetCorrectorParametersCollection> jetCorrParameters;
  // get the jet corrector parameters collection from the global tag
  setup.get<JetCorrectionsRecord>().get(payload_, jetCorrParameters);
  // get the uncertainty parameters from the collection
  JetCorrectorParameters const & param = (*jetCorrParameters)["Uncertainty"];
  JetCorrectionUncertainty* deltaJEC = new JetCorrectionUncertainty(param);
  //loop and rescale jets
  double dPx = 0., dPy = 0.;
  for(std::vector<pat::Jet>::const_iterator jet=jets->begin(); jet!=jets->end(); ++jet){
    pat::Jet scaledJet = *jet;
    //Jet resolution and scale factors
    JME::JetParameters parameters_5 = {{JME::Binning::JetPt, scaledJet.pt()}, {JME::Binning::JetEta, scaledJet.eta()}, {JME::Binning::Rho, *rho}};
    float rel_sig_pt = resolution.getResolution(parameters_5);
    //std::cout<<"rel_sig_pt = "<<rel_sig_pt<<std::endl;
    //JER scaled for all possible methods
    double jerScaleFactor = resolutionFactor(scaledJet, rel_sig_pt);
    scaleJetEnergy( scaledJet, jerScaleFactor );
    //----------------------------------
    //JES up/down 
    //additional JES unc from Top group
    //----------------------------------
    if(scaleType_.substr(0, scaleType_.find(':'))=="jes"){
      // instantiate the jec uncertainty object
      deltaJEC->setJetEta(jet->eta()); deltaJEC->setJetPt(jet->pt()); 
      // scale jet energy
      float jetMet = 0.0;
      jetMet = deltaJEC->getUncertainty(true); 
      if(scaleType_.substr(scaleType_.find(':')+1)=="up"){
        scaleJetEnergy( scaledJet, 1+jetMet);
      }
      else if(scaleType_.substr(scaleType_.find(':')+1)=="down"){
        scaleJetEnergy( scaledJet, 1-jetMet);
      }
    }
    pJets->push_back( scaledJet );
    //for MET correction
    dPx    += scaledJet.px() - jet->px();
    dPy    += scaledJet.py() - jet->py();
  }
  delete deltaJEC;
  //----------------------------------
  // scale MET accordingly
  //----------------------------------
  pat::MET met = *(mets->begin());
  double scaledMETPx = met.px() - dPx;
  double scaledMETPy = met.py() - dPy;
  double scaledMETE = sqrt(scaledMETPx*scaledMETPx+scaledMETPy*scaledMETPy);
  met.setP4(reco::MET::LorentzVector(scaledMETPx, scaledMETPy, 0, scaledMETE));
  pMETs->push_back( met );
  event.put(pJets, outputJets_);
  event.put(pMETs, outputMETs_);
}

double JetEnergyScale::resolutionFactor(const pat::Jet& jet, const double & rel_sig_pt){
  //----------------------------------
  // No JER for Data
  //----------------------------------
  if(!jet.genJet()) { return 1.; }
  // check if vectors are filled properly
  if((2*resolutionFactor_.size())!=resolutionRanges_.size()){
    // eta range==infinity
    if(resolutionFactor_.size()==resolutionRanges_.size()&&resolutionRanges_.size()==1&&resolutionRanges_[0]==-1.){
      resolutionRanges_[0]=0;
      resolutionRanges_.push_back(-1.);
    }
    // others
    else{
      edm::LogError msg("JetEnergyResolution");
      msg << "\n resolutionEtaRanges or resolutionFactors in module JetEnergyScale not filled properly.\n";
      msg << "\n resolutionEtaRanges needs a min and max value for each entry in resolutionFactors.\n";
      throw cms::Exception("invalidVectorFilling");
    }
  }
  //----------------------------------
  //calculate eta dependent JER SF
  //----------------------------------
  double sf = 1.;
  for(unsigned int n=0; n<resolutionFactor_.size(); ++n){
    int etaMin = 2*n;
    int etaMax = etaMin+1;
    if(std::abs(jet.eta())>=resolutionRanges_[etaMin]&&(std::abs(jet.eta())<resolutionRanges_[etaMax]||resolutionRanges_[etaMax]==-1.)){
      sf*=resolutionFactor_[n];
      // take care of negative scale factors 
      if(resolutionFactor_[n]<0){
	edm::LogError msg("JetEnergyResolution");
	msg << "\n chosen scale factor " << resolutionFactor_[n] << " is not valid, must be positive.\n";
	throw cms::Exception("negJERscaleFactors");
      }
    }
  }
  //----------------------------------
  //calculate pt smearing factor
  //----------------------------------
  double jet_pt = jet.pt();
  double gen_pt = jet.genJet()->pt();
  double deta = TMath::Abs(jet.eta() - jet.genJet()->eta());
  double dphi = TMath::Abs(jet.phi() - jet.genJet()->phi());
  if(dphi > M_PI) dphi = 2*M_PI - dphi;
  double delR = sqrt(deta*deta + dphi*dphi);
  double rCone = 0.4;
  double factor = 1.0;
  if(delR<rCone/2 && abs(jet_pt -gen_pt)<3*rel_sig_pt*jet_pt){
    factor = 1. + (sf-1.)*(jet_pt - gen_pt)/jet_pt;
  }
  return (factor<0 ? 0. : factor);
}

void JetEnergyScale::scaleJetEnergy(pat::Jet& jet, const double &factor)
{
  jet.scaleEnergy( factor ); // this will scale all the attributes of jet
  //undo the changes for various energy fractions
  if(jet.isPFJet()){ 
    pat::PFSpecific specificPF = jet.pfSpecific();
    specificPF.mChargedHadronEnergy = factor * specificPF.mChargedHadronEnergy;
    specificPF.mNeutralHadronEnergy = factor * specificPF.mNeutralHadronEnergy;
    specificPF.mPhotonEnergy        = factor * specificPF.mPhotonEnergy       ;
    specificPF.mElectronEnergy      = factor * specificPF.mElectronEnergy     ;
    specificPF.mMuonEnergy          = factor * specificPF.mMuonEnergy         ;
    specificPF.mHFHadronEnergy      = factor * specificPF.mHFHadronEnergy     ;
    specificPF.mHFEMEnergy          = factor * specificPF.mHFEMEnergy         ;
    specificPF.mChargedEmEnergy     = factor * specificPF.mChargedEmEnergy    ;
    specificPF.mChargedMuEnergy     = factor * specificPF.mChargedMuEnergy    ;
    specificPF.mNeutralEmEnergy     = factor * specificPF.mNeutralEmEnergy    ;
    jet.setPFSpecific(specificPF);
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE( JetEnergyScale );
