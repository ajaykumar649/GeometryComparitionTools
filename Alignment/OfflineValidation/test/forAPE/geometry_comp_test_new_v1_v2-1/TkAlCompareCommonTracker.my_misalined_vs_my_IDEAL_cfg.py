
import FWCore.ParameterSet.Config as cms

process = cms.Process("validation")

# global tag
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag.globaltag = "MCRUN2_74_V4::All" 
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_design', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_50ns', '')
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")

#process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")
process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")

#process.load("Alignment.CommonAlignmentProducer.GlobalPosition_Frontier_cff")
# the input .GlobalPosition_Frontier_cff is providing the frontier://FrontierProd/CMS_COND_31X_ALIGNMENT in the release which does not provide the ideal geometry
#process.GlobalPosition.connect = 'frontier://FrontierProd/CMS_COND_31X_FROM21X'

process.load("CondCore.DBCommon.CondDBSetup_cfi")

process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring('detailedInfo', 
        'cout')
)

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.load("DQM.SiStripCommon.TkHistoMap_cfi")

process.DQMStore=cms.Service("DQMStore")
#process.TkDetMap = cms.Service("TkDetMap")
#process.SiStripDetInfoFileReader = cms.Service("SiStripDetInfoFileReader")

process.load("DQMServices.Core.DQMStore_cfg") 
#process.DQMStore=cms.Service("DQMStore")

  # configuration of the Tracker Geometry Comparison Tool
  # Tracker Geometry Comparison
process.load("Alignment.OfflineValidation.TrackerGeometryCompare_cfi")
  # the input "IDEAL" is special indicating to use the ideal geometry of the release

process.TrackerGeometryCompare.inputROOTFile1 = 'my_misalinedROOTGeometry.root'
process.TrackerGeometryCompare.inputROOTFile2 = 'my_IDEALROOTGeometry.root'
# process.TrackerGeometryCompare.outputFile = "/tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160/my_misalined_vs_my_IDEAL.Comparison_commonTracker.root"
process.TrackerGeometryCompare.outputFile = "my_misalined_vs_my_IDEAL.Comparison_commonTracker.root"

process.load("CommonTools.UtilAlgos.TFileService_cfi")  
#process.TFileService = cms.Service("TFileService",
#		fileName = cms.string('TkSurfDeform.root') 
#		)
process.TFileService.fileName = cms.string("TkSurfDeform_my_misalined_vs_my_IDEAL.Comparison_commonTracker.root") 

process.TrackerGeometryCompare.levels = [ "Tracker","DetUnit" ]

  ##FIXME!!!!!!!!!
  ##replace TrackerGeometryCompare.writeToDB = false
  ##removed: dbOutputService

process.p = cms.Path(process.TrackerGeometryCompare)
