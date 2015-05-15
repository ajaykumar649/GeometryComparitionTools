
#!/bin/bash
CWD=`pwd -P`
source /afs/cern.ch/cms/caf/setup.sh
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src
export SCRAM_ARCH=slc6_amd64_gcc491
eval `scramv1 ru -sh`
# rfmkdir -p /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160
# rfmkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1

if [[ $HOSTNAME = lxplus[0-9]*\.cern\.ch ]] # check for interactive mode
then
    rfmkdir -p /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160
    rm -f /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160/*
    cd /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160
else
    mkdir -p $CWD/TkAllInOneTool
    cd $CWD/TkAllInOneTool
fi

# rm -f /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160/*
# cd /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160

#run
pwd
df -h .
#run configfile and post-proccess it
cmsRun /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/test/forAPE/geometry_comp_test_new_v1_v2-1/TkAlCompareToNTuple.my_misalined.7753626160_cfg.py
rfcp *.db /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1
 #run configfile and post-proccess it
cmsRun /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/test/forAPE/geometry_comp_test_new_v1_v2-1/TkAlCompareToNTuple.my_IDEAL.7753626160_cfg.py
rfcp *.db /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1
 #run configfile and post-proccess it
cmsRun /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/test/forAPE/geometry_comp_test_new_v1_v2-1/TkAlCompareCommonTracker.my_misalined_vs_my_IDEAL_cfg.py
rfcp *.db /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1
 # overall postprocessing
rfcp /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/scripts/comparisonScript.C .
rfcp /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/scripts/GeometryComparisonPlotter.h .
rfcp /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/scripts/GeometryComparisonPlotter.cc .
root -b -q 'comparisonScript.C+("my_misalined_vs_my_IDEAL.Comparison_commonTracker.root","./")'
rfmkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images
find . -maxdepth 1 -name "*PXB*" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "*PXF*" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "*TEC*" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "*TIB*" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "*TID*" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "*TOB*" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "*tracker*" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "plot*.eps" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "plot*.pdf" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "TkMap_SurfDeform*.pdf" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
find . -maxdepth 1 -name "TkMap_SurfDeform*.png" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/" 
if [[ $HOSTNAME = lxplus[0-9]*\.cern\.ch ]]
then
    rfmkdir -p /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160/my_misalined_vs_my_IDEAL.Tracker_ArrowPlots
else
    mkdir -p $CWD/TkAllInOneTool/my_misalined_vs_my_IDEAL.Tracker_ArrowPlots
fi
rfcp /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/scripts/makeArrowPlots.C .
root -b -q 'makeArrowPlots.C("my_misalined_vs_my_IDEAL.Comparison_commonTracker.root","my_misalined_vs_my_IDEAL.Tracker_ArrowPlots")'
rfmkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/ArrowPlots
find my_misalined_vs_my_IDEAL.Tracker_ArrowPlots -maxdepth 1 -name "*.png" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1/my_misalined_vs_my_IDEAL.Comparison_commonTracker_Images/ArrowPlots"
cmsStage -f OUTPUT_comparison.root /store/caf/user/ajkumar/AlignmentValidation/geometry_comp_test_new_v1_v2-1/comparedTracker_my_misalined_vs_my_IDEAL.root


echo "----"
echo "List of files in $(pwd):"
ls -ltr
echo "----"
echo ""


#retrieve
rfmkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/test/forAPE/geometry_comp_test_new_v1_v2-1 >&! /dev/null
gzip -f LOGFILE_*_my_misalined_vs_my_IDEAL.log
find /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160 -maxdepth 1 -name "LOGFILE*my_misalined*" -print | xargs -I {} bash -c "rfcp {} /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/test/forAPE/geometry_comp_test_new_v1_v2-1"

#copy root files to eos
cmsMkdir /store/caf/user/$USER/AlignmentValidation/geometry_comp_test_new_v1_v2-1
root_files=$(ls --color=never -d *my_misalined*.root)
echo ${root_files}

for file in ${root_files}
do
    cmsStage -f ${file} /store/caf/user/$USER/AlignmentValidation/geometry_comp_test_new_v1_v2-1
    echo ${file}
done

#cleanup
if [[ $HOSTNAME = lxplus[0-9]*\.cern\.ch ]] # check for interactive mode
then
    rm -rf /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160
fi
echo "done."
