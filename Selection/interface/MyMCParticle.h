#ifndef __MYMCPARTICLE_H__
#define __MYMCPARTICLE_H__

#include "TROOT.h"
#include <map>
#include <vector>
#include <string>

#include "MomentumVec.h"

class MyMCParticle 
{
 public:
  MyMCParticle();
  ~MyMCParticle();
  
  void Reset();
  MyLorentzVector p4Gen;
  int         pid;
  int     status;
  int     isLastCopy;

 private :

};
#endif
