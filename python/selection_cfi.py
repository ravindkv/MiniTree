import FWCore.ParameterSet.Config as cms

from MiniTree.ObjectSelectors_cfi import *

# all event filter
allEventsFilter = cms.EDFilter(
    "AllEventsFilter"
    )

# base configuration ----------------------------------------
myMiniTreeProducer = cms.EDAnalyzer("MiniTreeProducer",
                                    MCTruth = BaseMCTruthSet,
                                    Trigger = BaseTriggerSet,
                                    Vertex = BaseVertexSet,
                                    Tracks = BaseTrackSet,
                                    Muons = BaseMuonsSet,
                                    Electrons = BaseElectronsSet,
                                    Jets = BaseJetsSet,
                                    Mets = BaseMetsSet,
                                    KineFit = BaseKFPSet,
                                    rhoCorSrc = cms.InputTag("kt6PFJetsForIso","rho"),
                                    minEventQualityToStore = cms.int32(0)
                                    )

