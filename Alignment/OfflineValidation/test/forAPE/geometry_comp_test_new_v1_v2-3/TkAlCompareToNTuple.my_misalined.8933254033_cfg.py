
import FWCore.ParameterSet.Config as cms

process = cms.Process("ValidationIntoNTuples")

# global tag
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag.globaltag = "MCRUN2_74_V4::All" 
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_design', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_50ns', '')

#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
#process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")
#process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")
process.load("Geometry.TrackerGeometryBuilder.trackerGeometryDB_cfi")

#process.load("Alignment.CommonAlignmentProducer.GlobalPosition_Frontier_cff")
process.load("CondCore.DBCommon.CondDBSetup_cfi")

process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring('detailedInfo', 
        'cout')
) 



process.source = cms.Source("EmptySource",
    firstRun=cms.untracked.uint32(1)
    )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.dump = cms.EDAnalyzer("TrackerGeometryIntoNtuples",
    # outputFile = cms.untracked.string('/tmp/$USER/geometry_comp_test_new_v1_v2-3/8933254033/my_misalinedROOTGeometry.root'),
    outputFile = cms.untracked.string('my_misalinedROOTGeometry.root'),
    outputTreename = cms.untracked.string('alignTree')
)

process.p = cms.Path(process.dump)  
