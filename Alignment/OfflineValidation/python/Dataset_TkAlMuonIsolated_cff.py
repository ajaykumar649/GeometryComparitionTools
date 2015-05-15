import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/006CAB77-ED6F-E411-AD4F-00261894394D.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/02F01CF3-ED6F-E411-BC31-0025905964CC.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/04870CBE-F46F-E411-A2BF-0025905A48BC.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/06A9C33B-F16F-E411-A871-003048FFD730.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/0AF6FF4B-F46F-E411-A3AD-0025905938B4.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/1E66BC40-F16F-E411-A237-0025905B8596.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/36EDC9CE-ED6F-E411-A37E-0025905A60B4.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/3A64BA77-ED6F-E411-B355-003048FFD7C2.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/582D6541-EC6F-E411-9B95-0025905B8598.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/6271F6BA-F26F-E411-A162-0025905A6132.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/640CD6E7-5F77-E411-9AD2-0025905A6118.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/6656F731-F16F-E411-9142-002618FDA210.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/68F1C286-ED6F-E411-BC2A-0025905A48FC.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/8AB13B41-F16F-E411-ADDA-0025905A48F0.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/8CBAA427-EC6F-E411-80F0-0025905B857C.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/9A37DE3A-F16F-E411-BD07-0025905A60CA.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/B43478AE-5370-E411-A179-0025905A6076.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/B4CC90CD-ED6F-E411-B114-003048FFD7BE.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/E856B0AC-5370-E411-830C-002618943831.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/ECC79A37-F16F-E411-B498-0025905964BA.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/00000/F64C50C9-ED6F-E411-BEC1-002618943870.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/0C282185-ED6F-E411-A377-0026189438AE.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/0CD3D287-ED6F-E411-A089-003048FF86CA.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/1283381B-EE6F-E411-9E19-003048FFD76E.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/34F4E580-ED6F-E411-9205-002590596484.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/58E675BE-FA6F-E411-8C3E-0026189437F0.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/5ED3D43C-FD6F-E411-8A43-0025905B860C.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/6AFBAE58-FB6F-E411-ADD5-0026189438A5.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/70032187-ED6F-E411-9327-0025905B859E.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/765F0B92-F06F-E411-9314-00261894388B.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/7A29FA38-F66F-E411-B201-0025905A48F0.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/80C5BD50-F66F-E411-9671-0025905B860C.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/8E400480-ED6F-E411-8634-002590593920.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/96E16B12-F06F-E411-AD8F-0025905A60D6.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/A03F855B-F36F-E411-97D2-0025905B857C.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/A60DC58E-ED6F-E411-8B16-0025905A4964.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/AA7D2980-FB6F-E411-A339-0025905A60DA.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/ACB9452E-5C70-E411-AB0D-0025905A60AA.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/B053F095-FC6F-E411-80A7-002618943923.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/C44E0B2F-5C70-E411-B0BD-002590593920.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/C4A961CE-F26F-E411-B797-0025905B8610.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/D0B4D853-F36F-E411-ADE3-00261894397E.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/D227D088-ED6F-E411-A1FC-00261894388D.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/D25C8E24-0970-E411-8CF4-0025905A609A.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/D4041727-0170-E411-B994-002590593878.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/DEF4D489-F06F-E411-B0F2-003048FFD728.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/E4F6BE21-EE6F-E411-AA84-0025905A60CE.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/F067AC5E-FB6F-E411-8021-0025905A6060.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/F8B3CD03-F06F-E411-B800-0025905A48BA.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/FAB124CA-FA6F-E411-8369-0025905B8572.root',
       '/store/mc/Phys14DR/WJetsToLNu_13TeV-madgraph-pythia8-tauola/ALCARECO/TkAlMuonIsolated-PU20bx25_PHYS14_25_V1-v1/10000/FEDE39AF-F26F-E411-B54D-0025905A611E.root' ] );


secFiles.extend( [
               ] )

