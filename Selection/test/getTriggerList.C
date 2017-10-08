#include <fstream>
void getTriggerList()
{
  TFile f1("outFile_.root");
  TH1F* h1 = (TH1F*)f1.Get("myMiniTreeProducer/trigger/trigger_bitsrun");
  ofstream out;
  out.open("trigPathsMC.txt");
  //out.open("trigPathsData.txt");
  cout<<" file opned"<<endl;
  //  f1.ls(); 
  //  gSystem->Exit(0);
  
  for(int i = 1; i <= h1->GetXaxis()->GetNbins(); i++){
    out<<h1->GetXaxis()->GetBinLabel(i)<<endl;
    //cout<<h1->GetXaxis()->GetBinLabel(i)<<endl;
  }
  out.close();
 /*
  std::vector<string> trigName;
  trigName.push_back("cms_");
  trigName.push_back("atlas2");
  trigName.push_back("cern");

  std::vector<string> myTrigNames;
  //myTrigNames.push_back("cms_v");
  //myTrigNames.push_back("atlas");
  //myTrigNames.push_back("cern");
  
  myTrigNames.push_back("cms_v");
  myTrigNames.push_back("atlas");
  myTrigNames.push_back("cern");

  for(int i =0; i<trigName.size(); i++){
    cout<<"trigName befor for = "<<trigName[i]<<endl;
    if(std::find(myTrigNames.begin(), myTrigNames.end(), trigName[i]) == myTrigNames.end()) {//continue;

// if(trigName[i].find(myTrigNames[0])==std::string::npos || trigName[i].find(myTrigNames[1])==std::string::npos ||trigName[i].find(myTrigNames[2])==std::string::npos){
  cout<<i<<endl;
  cout<<"trigName = "<<trigName[i]<<endl;
  }
  }
  */
}
