#include "MiniTree/Selection/interface/MySampleInfo.h"

MySampleInfo::MySampleInfo()
{
  sampleName="";
  mcEvtType = 0;
  pileup.clear();
  truepileup.clear();
  ///puWeights.clear();
  ///truepuWeights.clear();
  hepNUP = -99;
  hepIDUP.clear();
  hepISTUP.clear();
}

MySampleInfo::~MySampleInfo()
{
}
