import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/621/00000/A201CA90-D969-E411-ACAB-02163E010E1C.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/632/00000/445E8C20-D969-E411-8964-02163E010ED5.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/653/00000/0A195DA6-D969-E411-96F9-02163E010CD2.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/665/00000/381229C0-DB69-E411-A00C-02163E010F2D.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/666/00000/82A0183F-DB69-E411-B811-02163E010CC2.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/667/00000/C6FBA737-DC69-E411-B24E-02163E00FFD0.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/669/00000/AEE1F20B-DB69-E411-8C5A-02163E010CBC.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/672/00000/96584780-DB69-E411-B55B-02163E010CC7.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/680/00000/420D78D6-DA69-E411-BC77-02163E010CD6.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/684/00000/C8BA3687-EC69-E411-92D9-02163E010D45.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/685/00000/CE4A8B46-1F6A-E411-9CE6-02163E010BED.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/695/00000/12E0A719-1A6A-E411-9C8B-02163E010CC2.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/699/00000/625EFFCA-1F6A-E411-9ACD-02163E010DD8.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/702/00000/D41664F5-1F6A-E411-818A-02163E010ECB.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/708/00000/807214C5-1A6A-E411-A3EF-02163E010CC0.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/709/00000/3EFEF85F-836A-E411-A634-02163E00FB9F.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/712/00000/CCE92AE1-6F6A-E411-A7E2-02163E010C03.root', 
'/store/data/Commissioning2014/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v4/000/229/713/00000/C87DAE0C-9A6A-E411-A977-02163E010EB4.root',] );


secFiles.extend( [
               ] )
