#include "MiniTree/Selection/interface/MyVertex.h"

MyVertex::MyVertex():
  chi2(-9),
  isValid(-1),
  ndof(0),
  normalizedChi2(-9),
  rho(-9)
{
}

MyVertex::~MyVertex()
{
}

void MyVertex::Reset()
{
  chi2 = -9;
  ErrXYZ.SetCoordinates(0.0,0.0,0.0);
  isValid = -1;
  ndof = 0;
  normalizedChi2 = -9.;
  rho = -9;
  rhoAll_ = -9;
  XYZ.SetCoordinates(0.0,0.0,0.0);
}
