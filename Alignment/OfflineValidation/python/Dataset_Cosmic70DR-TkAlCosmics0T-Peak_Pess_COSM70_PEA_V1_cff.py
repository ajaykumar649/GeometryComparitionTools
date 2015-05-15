import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/02C82C6D-1B63-E411-AACD-001E673968F1.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/0C101358-1B63-E411-9742-0025B3E06466.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/10F5FBBD-1A63-E411-8788-001E67398DE5.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/1612EDE0-1A63-E411-86BA-001E67397BC5.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/2468EB92-1A63-E411-9425-002481E14FFC.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/2E5BDA92-1A63-E411-8698-001E673984C1.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/38C77694-1A63-E411-B47E-002590A80D9C.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/3ADBFC8E-1A63-E411-A7DF-002590A3A3D2.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/3C882490-1A63-E411-B87A-001E67398683.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/40B484B9-1A63-E411-BE89-001E67397AD0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/46C2DB06-1C63-E411-8952-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/46F20694-1A63-E411-8698-001E67397F35.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/4EF56B8D-1A63-E411-BCE9-001E67397BC5.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/5292652F-1A63-E411-9315-001E67397D05.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/54A1F0C4-1A63-E411-BF41-002590A831B6.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/5E638EE2-1A63-E411-A7E4-001E67397AE4.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/6498009A-1A63-E411-98B1-001E673972AB.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/6C67CE4F-1A63-E411-8408-001E67397F3F.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/720BBAB9-1A63-E411-B90E-001E67398791.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/765C4BE2-1A63-E411-A0AA-001E67397AE4.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/82663BC8-1A63-E411-B06F-002590A3A3D2.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/828C0F8D-1A63-E411-947C-002590A80DF0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/8A0F0990-1A63-E411-B67C-001E67397B1B.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/92059592-1A63-E411-B9F8-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/943A965A-1A63-E411-BB6A-002590A371D4.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/985BA3A0-1A63-E411-BE72-0025B3E05CDA.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/9C73DC96-1A63-E411-BC56-0025B3E0653E.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/9ECB798B-1A63-E411-8D66-001E67397F3F.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/A2805C9A-1A63-E411-8495-0025B3E065CA.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/A45CCE4F-1A63-E411-BD27-001E67397F3F.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/AE79C44B-1A63-E411-B1FA-001E67397008.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/B0BE8FBB-1A63-E411-A248-002590A887F8.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/B42D9494-1A63-E411-ABAD-0025B3E063A0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/B44D44BA-1A63-E411-BF28-001E67397008.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/B6F7F994-1A63-E411-B5B9-001E67396A63.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/B8FA7253-1A63-E411-BF29-002481E7451E.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/C071E0FC-1A63-E411-9116-001E67397AE4.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/C0C65277-1A63-E411-BEE8-001E67397AD0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/C0E137FE-1A63-E411-B1CC-001E67398DE5.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/C2DAD4DD-1B63-E411-A369-002590A80DF0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/C4779F93-1A63-E411-ADE1-0025B3E05BC4.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/C4E78D4E-1A63-E411-AECD-002590200AF4.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/C673A58F-1A63-E411-8CC0-001E67398DE5.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/C6CC7386-1A63-E411-A135-001E673968F1.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/C8D45D88-1A63-E411-8BB9-001E67398791.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/D8E51384-1A63-E411-8A8D-001E67397008.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/DE511458-1A63-E411-ADCF-0025B31E3C28.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/E07EF3E4-1A63-E411-881E-001E67397CAB.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/E2945BBF-1A63-E411-8E3D-001E67396685.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/00000/E8E2377A-1B63-E411-A20F-0025902009C8.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/02828B70-4A63-E411-BA71-002590A50046.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/063C41C5-4A63-E411-A57E-002590A831CC.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/08F03C2D-4A63-E411-9EF4-002590A831B6.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/0CB733E8-4A63-E411-9686-002590A80DF0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/0E60B994-4A63-E411-94C4-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/1A9B75CD-4A63-E411-B3D8-002590A3711E.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/202F8975-4A63-E411-AB43-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/24D95E24-4A63-E411-BA1C-002590A831B6.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/2AA5B0BE-4A63-E411-B559-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/2E2627EB-4A63-E411-AEE4-002590A3C970.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/3672D6BF-4A63-E411-85A7-002590A37116.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/3E813A90-4A63-E411-87DB-002590A831CC.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/462A5A3D-4A63-E411-BB00-002590A50046.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/4679F926-4A63-E411-A038-002590A81DAC.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/48ED17C4-4A63-E411-BD61-002590A81DAC.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/54454DE4-4A63-E411-993A-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/5C2B03EB-4A63-E411-9194-002590A3C970.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/5C9F218B-4A63-E411-A999-002590A3C970.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/6EAB1406-4B63-E411-8241-001E673970FD.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/70083280-4A63-E411-AC84-002590A3711E.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/74427D88-4A63-E411-9485-002590A80DF0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/7C8D6575-4A63-E411-8CA4-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/96CF3B25-4A63-E411-B9FD-002590A3C970.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/981F14EB-4A63-E411-8D5B-002590A3C970.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/A0E93C2D-4A63-E411-9390-002590A831B6.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/A246EB7E-4A63-E411-BD4B-002590A83174.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/A2C15445-4A63-E411-BAFC-002590A3707C.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/A6FA0C50-4A63-E411-B322-002590A50046.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/A8D87B33-4A63-E411-8EA8-002590A887F2.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/B26932B9-4A63-E411-BEC8-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/B862BE88-4A63-E411-85F2-002590A83174.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/BC3CF68A-4B63-E411-8631-002590A887F8.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/C28397C5-4A63-E411-B953-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/C6B4F78A-4A63-E411-B7BF-002590A3C970.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/CA70BE36-4A63-E411-BF4D-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/CC5881FC-4A63-E411-9E69-002590A50046.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/D46BED8E-4A63-E411-9839-002590A50046.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/D67057B9-4A63-E411-A91C-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/D6BB6CBD-4A63-E411-A3AE-002590A83136.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/DAC0BD36-4A63-E411-A40C-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/DEC4172F-4A63-E411-A9B5-002590A3C970.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/E00223FC-4A63-E411-9058-002590A50046.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/E268E388-4A63-E411-9902-002590A37116.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/E6528972-4A63-E411-9698-002590A83308.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/E855808F-4A63-E411-ACC6-002590A831CC.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/F2A5A349-4A63-E411-A8AC-001E67396928.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/FAAC1545-4B63-E411-B2F7-002590A887F8.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/FCD6DBCB-4A63-E411-B215-002590A3707C.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/FE451482-4A63-E411-AA8A-002590A50046.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/10000/FEC1D526-4A63-E411-82F2-002590A81DAC.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/106C381F-4763-E411-AAE9-002590A37106.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/12A12AD3-4663-E411-90DA-002590A80DF0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/3C13AD96-4663-E411-B81E-002590A80DF0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/3E691897-4663-E411-A301-002590A80DF0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/4CBD84D7-4663-E411-88A5-001E673975EE.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/5AF51998-4663-E411-8378-001E673975EE.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/66EA8147-4763-E411-8E31-001E67398DE5.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/6EB430D6-4663-E411-856D-001E673975EE.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/8671CF75-4763-E411-8E6E-002590A4FFA2.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/8A6210D2-4663-E411-B6B0-002590A80DF0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/8E821C98-4663-E411-81A3-001E673975EE.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/AC5F90D3-4663-E411-9CF8-002590A80DF0.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/B6AFC6E8-4663-E411-8C95-002590A80DF4.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/CE3F7B9B-4663-E411-9919-002590A80DF4.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/D0C97758-4763-E411-A18E-002590A3716C.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/D4931542-4763-E411-99C1-001E67398DE5.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/E24D233A-4763-E411-87F5-002590A831CC.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/F2A872C0-4763-E411-9F47-002590A88812.root',
       '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Pess_COSM70_PEA_V1-v1/20000/FAC2627C-4763-E411-9A7D-001E67397314.root' ] );


secFiles.extend( [
               ] )

