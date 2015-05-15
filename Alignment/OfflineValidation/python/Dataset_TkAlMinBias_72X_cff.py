import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/02405CE0-8E6B-E411-A37C-20CF3019DF03.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/061BE8BE-276B-E411-8F53-002590D0AFE6.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/34856B99-866B-E411-B284-002590747E0E.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/4E069989-826B-E411-87BB-E0CB4E19F9BC.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/4E35BE7D-806B-E411-81EE-E0CB4E553642.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/58580529-896B-E411-B2A1-00248C9BA537.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/6C2E6B14-7B6B-E411-B3F2-0025907B4FB6.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/7244288A-8B6B-E411-A27D-20CF305B0556.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/726A92D5-7D6B-E411-B407-E0CB4E29C502.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/9035D670-836B-E411-9B47-0025907B4F8A.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/9C1A84DF-F36A-E411-9271-E0CB4E5536A7.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/A477E653-766B-E411-BE2B-E0CB4E553665.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/A4F802A1-7C6B-E411-805C-E0CB4EA0A931.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/B6288611-796B-E411-A3E9-E0CB4EA0A91C.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/BC79E75B-AD6B-E411-8AF9-20CF3027A5B9.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/DE4D62FB-7E6B-E411-8653-E0CB4E19F95B.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/E4F6FD06-5B6B-E411-BF0A-002590D0B03E.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/FC3F4FAB-816B-E411-AD20-002590D0AFEA.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/02812CCB-8D6B-E411-B4C1-002590D0B09C.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/0CDC8182-676B-E411-9198-002590D0B080.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/205BCAA0-866B-E411-8D62-002590D0B046.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/2273F1B8-7D6B-E411-AB97-002590D0B0C8.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/285B9380-8A6B-E411-8CD9-20CF3019DF11.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/32829E24-556B-E411-830F-0025907B4F3A.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/50F2DCEA-766B-E411-92C7-20CF3027A5BC.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/5E50D7CC-746B-E411-8BF2-002590D0B072.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/72F12B96-6F6B-E411-BC0D-E0CB4EA0A91E.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/7E2A0304-956B-E411-B793-0025907B4F7A.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/8C608CCC-7C6B-E411-814B-002590D0B0A4.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/AA542C05-836B-E411-870B-00259074AE28.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/ACE249AA-806B-E411-B05C-002590D0AF9A.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/AEA6D537-386B-E411-95F4-00259073E34E.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/B2D33E33-7F6B-E411-A0BB-20CF3019DEE8.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/C0849850-7B6B-E411-B816-0025907B4F4E.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/DC4AB087-816B-E411-B831-E0CB4E5536A5.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/DC525CA5-786B-E411-8E6E-002590D0B052.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/DE962424-826B-E411-8BBA-002590D0B0B2.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/E229E326-7A6B-E411-8356-0025907B4F00.root',
       '/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/ALCARECO/TkAlMinBias-PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/F830D33C-846B-E411-BEF4-00259073E534.root' ] );


secFiles.extend( [
               ] )
