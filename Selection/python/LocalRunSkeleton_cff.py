import FWCore.ParameterSet.Config as cms
# pat tuple modules -----------------------------------------------------------
from MiniTree.Selection.JetMETExtra_cff import *

#trigger match
from MiniTree.Selection.PATtriggerMatchExtra_cff import *

#muon config
from MiniTree.Selection.MuonExtra_cff import *

#electron config
from MiniTree.Selection.ElectronExtra_cff import *

#PFlow
from MiniTree.Selection.pfToPatSequences_cff import *

#generator level utils
from MiniTree.Selection.GeneratorLevelUtilities_cff import *

#TTBar Kinematic Fitter for lepton+Jets
#from MiniTree.Selection.ttSemiLepKinFitMuon_cff import *
#from MiniTree.Selection.ttSemiLepKinFitElectron_cff import *

#filter to count all events processed
process.load("MiniTree.Selection.alleventsfilter_cfi")
process.load("PhysicsTools.UtilAlgos.TFileService_cfi")
