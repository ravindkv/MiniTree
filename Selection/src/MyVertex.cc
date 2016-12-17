#include "MiniTree/Selection/interface/MyVertex.h"

MyVertex::MyVertex():
  chi2(-999),
  isValid(-1),
  ndof(0),
  normalizedChi2(-999),
  rho(-999)
{
}

MyVertex::~MyVertex()
{
}

void MyVertex::Reset()
{
  chi2 = -999;
  ErrXYZ.SetCoordinates(0.0,0.0,0.0);
  isValid = -1;
  ndof = 0;
  normalizedChi2 = -999.;
  rho = -999;
  XYZ.SetCoordinates(0.0,0.0,0.0);
}
