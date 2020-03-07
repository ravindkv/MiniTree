#include "MiniTree/Selection/interface/MyMCParticle.h"

MyMCParticle::MyMCParticle()
{
}
MyMCParticle::~MyMCParticle()
{
}
void MyMCParticle::Reset()
{
  p4Gen.SetCoordinates(0.0, 0.0, 0.0, 0.0);
  pid = 0;
  status = 0;
  isLastCopy = 0;
}
