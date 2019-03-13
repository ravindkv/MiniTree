import FWCore.ParameterSet.Config as cms

from MiniTree.Selection.ObjectSelectors_cfi import *

# all event filter
allEventsFilter = cms.EDFilter(
    "AllEventsFilter"
    )

# base configuration ----------------------------------------
myMiniTreeProducer = cms.EDAnalyzer("MiniTreeProducer",
                                    MCTruth = BaseMCTruthSet,
                                    Trigger = BaseTriggerSet,
                                    Vertex = BaseVertexSet,
                                    Muons = BaseMuonsSet,
                                    Electrons = BaseElectronsSet,
                                    Jets = BaseJetsSet,
                                    Mets = BaseMetsSet,
                                    KineFit = BaseKFPSet,
                                    minEventQualityToStore = cms.int32(0)
                                    )

