import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( ['/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/0079D989-6663-E411-833F-002590A371AA.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/0612FB82-6663-E411-BD85-002481E150FE.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/0E10D4B7-6663-E411-A376-001E67398A43.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/0E49B4E9-6663-E411-831A-0025B3E06548.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/0ED768C5-6663-E411-9F15-002481E150FE.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/1803DCF3-6663-E411-A2D4-0025902008FC.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/1C4E9CD5-6663-E411-AD34-001E67397D05.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/1CF75B9A-6663-E411-83F6-0025B3E06548.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/220FC73D-6763-E411-AB04-002590200A98.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/3C581FAB-6663-E411-A774-002590200B38.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/3CB0FDA6-6663-E411-9417-002481E75ED0.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/424F6201-6763-E411-B36E-0025B31E3C58.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/46C55147-6763-E411-B344-002590200B44.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/4AC6EAEF-6663-E411-B5E1-001E673971C5.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/4E77C579-6663-E411-ADC8-002590200B44.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/523F4CC6-6763-E411-8C86-002590A371CA.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/5679B7B9-6663-E411-BCC0-002590200AF4.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/5AA23036-6763-E411-A236-002590200918.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/5CC98A71-6763-E411-B14B-0025B3E063CA.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/7A358B92-6663-E411-A4AB-001E6739677A.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/8070760B-6763-E411-926A-002590A37118.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/82D3145E-6663-E411-B51C-001E673971C5.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/86BF06B3-6663-E411-86BA-001E67398110.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/88BC56F0-6663-E411-AC81-001E67398110.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/8A5F526D-6763-E411-9AEA-002590A88736.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/8E2BC462-6763-E411-92BC-002590A80DA4.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/A29341E7-6663-E411-9BC3-002481E75ED0.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/A80086E4-6663-E411-B7FD-001E6739677A.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/B242CFF9-6663-E411-8AB0-002590200868.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/BEE1CA20-6763-E411-8017-001E67396C52.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/BEEAE4B7-6663-E411-A99D-002590A83174.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/C8AEBCCB-6663-E411-820C-002590A8880A.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/CC8D3AC5-6663-E411-ACB9-002590200A94.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/D85D91F5-6763-E411-92F9-002590200858.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/E0408EC3-6663-E411-B9CE-002590A371AA.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/E206EE50-6663-E411-915F-0025B3E06548.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/E62AC0BF-6663-E411-8A84-0025B3E05CE4.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/F08D4667-6763-E411-AA9B-002590200A28.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/F0F5198C-6663-E411-98A9-0025B31E3C58.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/00000/F0F943F3-6763-E411-9E74-002590200B38.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/0C2297A3-6B63-E411-83DC-002590A80E1E.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/1892587F-6B63-E411-BE5E-002590A80DF0.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/1A620FA6-6B63-E411-92AB-001E67397B25.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/1EB34ACF-6B63-E411-AF3D-001E67398142.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/22B41A86-6C63-E411-A0E0-002590A4C6AE.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/241B1401-6C63-E411-A098-001E67397238.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/2499DDAA-6B63-E411-A831-002590200900.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/263D1CDF-6B63-E411-96AF-002590200988.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/30C104A5-6B63-E411-BD0F-002590A80E0A.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/3606F41E-6C63-E411-8517-001E6739726F.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/360B1AF9-6B63-E411-86E8-002590A80DF0.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/3AD36AA0-6B63-E411-A2D2-002590200B4C.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/50DB7927-6C63-E411-8036-002590A371C4.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/56A4A554-6C63-E411-A529-002590A88736.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/788B5E75-6B63-E411-B5B3-001E67396644.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/84AF30F0-6B63-E411-B3EE-002481E14F8C.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/8C43DC6C-6B63-E411-91CD-001E67397756.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/96FDA8B3-6B63-E411-8B02-002590A80E1C.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/A4EA4B7F-6B63-E411-8BFD-002590A80DF0.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/AE0BF41E-6C63-E411-A345-001E6739726F.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/B015AB89-6B63-E411-B735-001E67398CB9.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/B6BC5DC0-6B63-E411-8FD6-0025B31E3C00.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/BEF08683-6B63-E411-AB25-001E67398458.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/C41A07D8-6B63-E411-B176-0025B3E06508.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/C45C6BC8-6B63-E411-B296-002481E1501E.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/DA0B846D-6B63-E411-B126-001E67397E13.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/E655DE84-6C63-E411-9DED-002590A370FE.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/10000/F63916E6-6B63-E411-8161-0025B3E06612.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/0E1946A8-7863-E411-9935-0025902009BC.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/0EE2AF89-7863-E411-A338-001E673976ED.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/105F4ACF-7863-E411-8261-001E673967C5.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/124B2845-7863-E411-BD64-0025B3E05D3A.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/146891C2-7763-E411-84B4-0025B3E05D3A.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/18E7A7B5-7763-E411-9B09-001E6739801B.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/1C9DA278-7863-E411-A098-001E67397094.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/1E73CD9E-7763-E411-9840-002481E14F74.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/22D40C13-7863-E411-A96D-002590A36FB2.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/50207B02-7863-E411-BEAF-001E67397B25.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/5081B372-7863-E411-964E-001E67397B25.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/5230CFF6-7763-E411-A406-001E67397AE4.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/5472561C-7863-E411-B12A-0025B3E06394.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/645726B2-7763-E411-9063-0025902009BC.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/66F5103B-7863-E411-898A-001E67397C33.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/72E2B781-7863-E411-9168-001E67397EDB.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/7427D450-7863-E411-9FC4-0025B3E0650E.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/7451C2A6-7863-E411-AE58-001E6739830E.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/7A2BD211-7863-E411-BB2C-002481E150FC.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/7A53A3F9-7863-E411-9366-D8D385FF7678.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/8298BF6D-7863-E411-8E96-002590200B68.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/82AE69FD-7863-E411-B296-001E67398CA0.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/84BB5067-7863-E411-9837-001E6739801B.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/86BCDD18-7863-E411-8B3F-001E67397094.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/88070252-7863-E411-8A16-001E67397AE4.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/92532574-7863-E411-A4B7-001E67398228.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/928ABF07-7863-E411-877F-002481E15522.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/94FEF301-7963-E411-BBEB-002590A50046.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/9E0D7149-7863-E411-A4C0-0025B3E0654E.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/9E250BFC-7763-E411-B352-002481E14F74.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/9EA2D76B-7863-E411-8BAD-002590A83308.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/AAC2C9EE-7763-E411-BA39-002590A371D4.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/AEEB9CEE-7763-E411-92B3-001E67396707.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/B07A3A38-7863-E411-ADB0-0025B3E05C32.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/B42EE327-7863-E411-9AFB-002590A371D4.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/BA2F5B62-7863-E411-9B37-001E673976D9.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/C0F4152D-7863-E411-BE16-001E67398458.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/C28EA50B-7863-E411-A042-001E6739830E.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/C6945326-7863-E411-932C-F04DA23BBCCA.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/CC8EB406-7863-E411-AB17-001E673983A4.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/CE0CB977-7863-E411-B8A7-001E67396707.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/D045DD09-7863-E411-9BDF-001E6739801B.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/D0B32607-7863-E411-BFA9-D8D385FF7678.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/D686676F-7863-E411-8012-001E67397C79.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/D68839EB-7863-E411-98C2-001E67396AC2.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/E2A9FB9C-7863-E411-AF6C-9C8E991A143E.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/E67A7ED6-7863-E411-88C3-001E6739703A.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/EC8F28FE-7763-E411-8FA9-0025B3E05D3A.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/F21D0DD6-7763-E411-9B4E-002481E14F74.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/F6547127-7863-E411-BB14-0025B3E05D8C.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/F6DAB4FD-7863-E411-B02D-002590A83308.root',
                   '/store/mc/Cosmic70DR/TKCosmics_0T/ALCARECO/TkAlCosmics0T-Peak_Opti_COSM70_PEA_V2-v1/20000/FC45F781-7863-E411-ACA2-001E67397EDB.root'] );

secFiles.extend( [
               ] )
