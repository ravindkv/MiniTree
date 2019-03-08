#include "MiniTree/Selection/interface/MyEventSelection.h"

std::vector<std::string> MyEventSelection::getHLT(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  std::vector<std::string> hltPaths;
  hltPaths.clear();
  std::vector<std::string> myTrigBits = configParamshlt_.getParameter<std::vector<std::string> >("trigBits");
  std::vector<std::string> metFilterBits = configParamshlt_.getParameter<std::vector<std::string> >("metFilterBits");

  // MET filters
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#2016_data
  edm::Handle<edm::TriggerResults> hltResFilter;
  iEvent.getByToken(hltFilter_, hltResFilter); // 76x
  ////assert(hltResFilter.isValid());
  const edm::TriggerNames& allFilterNames = iEvent.triggerNames(*hltResFilter);
  bool filterMET = false;
  for(unsigned int i = 0; i<metFilterBits.size(); i++){
    string filterName = metFilterBits[i];
    if(allFilterNames.triggerIndex(filterName) < hltResFilter->size()){
      filterMET=hltResFilter->accept(allFilterNames.triggerIndex(filterName));
    }
  }
  // HLT selection
  edm::Handle<edm::TriggerResults> hltresults;
  iEvent.getByToken(hlt_, hltresults); // 76x
  ////assert(hltresults.isValid());
  const edm::TriggerNames& TrigNames_ = iEvent.triggerNames(*hltresults);
  const int ntrigs = hltresults->size();
  for (int itr=0; itr<ntrigs; itr++){
    if(!hltresults->wasrun(itr) )continue;
    if (!hltresults->accept(itr)) continue;
    bool passTrig = false;
    std::string trigName=TrigNames_.triggerName(itr);
    for(unsigned int i = 0; i<myTrigBits.size(); i++){
      if(trigName.find(myTrigBits[i]) != string::npos) passTrig = true;
    }
    if(passTrig && filterMET) hltPaths.push_back(trigName);
  }
  return hltPaths;
}
