import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
lumiSecs = cms.untracked.VLuminosityBlockRange()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles, lumisToProcess = lumiSecs)
readFiles.extend( [
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/02A475B4-FFEF-E311-B15C-002590A36FB2.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/0437559D-65F0-E311-AB44-002590A80DA4.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/0EEE9B30-B1F0-E311-9A1A-001E67397215.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/1055A8E6-DFF0-E311-903A-0025B3E05D0A.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/1607460E-31F0-E311-AFFB-002590A371AC.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/16875016-62F0-E311-B614-002590A37122.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/1AD44270-9DEF-E311-921F-002590200AB8.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/24A1702C-63F0-E311-AAEF-9C8E991A143E.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/24E80532-E1EF-E311-AA15-001E673968A6.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/2E07F1C1-ACEE-E311-B0A6-0025902008D8.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/3642274A-31F0-E311-9A4F-0025B3E0653E.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/368FA19E-06F0-E311-AA61-0025B3E063F0.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/369C17F4-00F0-E311-8126-002590A3707C.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/3AAF54B5-CEEE-E311-B499-002590A36F46.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/3E10D287-E0F0-E311-A81A-0025B3E063E8.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/40DB129E-AAEE-E311-8476-001E67398381.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/4C0C44C6-A4EF-E311-A7CE-002590A371C4.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/5618A87B-9DEF-E311-8616-002590A887AC.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/5CE8CF43-E0F0-E311-A915-0025B3E063E8.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/64E26A7A-F9EF-E311-9E55-0025B3E06394.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/7433602D-AEF0-E311-9C8E-0025B3E05D8C.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/7A0CC689-EFEF-E311-B1FC-002481E14E56.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/7C415E8F-1FF0-E311-B6F9-002590A37120.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/8A906DA0-9DEF-E311-9833-002590A831CC.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/90EAE214-62F0-E311-9B9A-001E67398E12.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/9431EE1B-AFF0-E311-ACBD-0025B3E05DD6.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/A4C8D3FB-E9F3-E311-86BF-002590200B78.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/A6DC503D-F1EF-E311-B828-002590A887F8.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/AA560282-E0F0-E311-9276-0025B3E063EA.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/ACF7605D-ABEE-E311-8A2E-002590A80D9C.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/B0382B2E-9AF2-E311-94CD-002590200AB8.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/B09FBC6C-9DEF-E311-9D61-002590A3716C.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/B65E9879-F9EF-E311-B85E-002590200808.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/B6C2CE21-C2EE-E311-9AF6-0025902009CC.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/B6E1E32C-63F0-E311-8ABF-002590A80DA4.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/B8DF3B17-17F0-E311-8BF1-001E673972E7.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/C21A58ED-16F0-E311-A1DD-001E67396793.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/C2C55CA5-E1EF-E311-85C9-002590A4FFC6.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/C2E23495-1FF0-E311-8C19-002481E1501E.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/C6145493-A5EE-E311-992E-001E67398CA0.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/CCA0142C-63F0-E311-A4B1-0025B3E0657E.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/DCBD0A63-4FF0-E311-8667-002590A831CA.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/E2567D01-F0EF-E311-AFC7-002590A36FB2.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/E25FF06B-4FF0-E311-AE78-0025B3E066A4.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/E84A32CD-9DEF-E311-97C3-002590A3C95E.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/E8E0EC29-63F0-E311-B16B-0025B3E06658.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/F07B399C-65F0-E311-88AD-984BE1089EB8.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/F2685105-E1F0-E311-AFB0-002590A887F2.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/FC826C16-F1EF-E311-8B37-002590A3C978.root',
       '/store/mc/Spring14dr/DYToMuMu_M-50_Tune4C_13TeV-pythia8/ALCARECO/TkAlMuonIsolated-castor_PU20bx25_POSTLS170_V5-v1/00000/FC901D8D-9DEF-E311-8FDF-002590200808.root'
] )

lumiSecs.extend([
])
