#include <fstream>

void getTriggerList()
{
  //  TFile f1("Monitor_254_1_sdA.root");
  TFile f1("mc_electron_May_2016.root");
  TH1F* h1 = (TH1F*)f1.Get("myMiniTreeProducer/trigger/trigger_bitsrun");
  ofstream out;
  out.open("trigPaths.txt");
  cout<<" file opned"<<endl;
  //  f1.ls(); 
  //  gSystem->Exit(0);
  
  for(int i = 1; i <= h1->GetXaxis()->GetNbins(); i++){
    out<<h1->GetXaxis()->GetBinLabel(i)<<endl;
    //cout<<h1->GetXaxis()->GetBinLabel(i)<<endl;
  }
  out.close();
}
