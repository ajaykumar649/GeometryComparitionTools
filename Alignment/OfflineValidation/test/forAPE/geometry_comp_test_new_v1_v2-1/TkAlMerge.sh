
#!/bin/bash
CWD=`pwd -P`
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src
export SCRAM_ARCH=slc6_amd64_gcc491
eval `scramv1 ru -sh`

#create results-directory and copy used configuration there
rfmkdir -p /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1
rfcp /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/test/forAPE/geometry_comp_test_new_v1_v2-1/usedConfiguration.ini /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/results/$USER/output_geometry_comparison/geometry_comp_test_new_v1_v2-1

if [[ $HOSTNAME = lxplus[0-9]*\.cern\.ch ]] # check for interactive mode
then
    mkdir -p /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160
    cd /tmp/$USER/geometry_comp_test_new_v1_v2-1/7753626160
else
    cd $CWD
fi
echo "Working directory: $(pwd -P)"

###############################################################################
# download root files from eos
root_files=$(cmsLs -l /store/caf/user/$USER/AlignmentValidation/geometry_comp_test_new_v1_v2-1 | awk '{print $5}'              | grep ".root$" | grep -v "result.root$")
for file in ${root_files}
do
    cmsStage -f ${file} .
    # echo ${file}
done


#run

#run comparisons
#merge for GeometryComparison.Tracker if it does not exist or is not up-to-date
echo -e "

Comparing validations"
cp /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/scripts/compareFileAges.C .
root -x -q -b -l "compareFileAges.C(\"root://eoscms.cern.ch//eos/cms/store/caf/user/$USER/AlignmentValidation/geometry_comp_test_new_v1_v2-1/GeometryComparison.Tracker_result.root\", \"root://eoscms.cern.ch//eos/cms/store/caf/user/ajkumar/AlignmentValidation/geometry_comp_test_new_v1_v2-1/comparedTracker_my_misalined_vs_my_IDEAL.root\")"
comparisonNeeded=${?}

if [[ ${comparisonNeeded} -eq 1 ]]
then
    cp /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/scripts/compareAlignments.cc .
    root -x -q -b -l 'compareAlignments.cc++("root://eoscms.cern.ch//eos/cms/store/caf/user/ajkumar/AlignmentValidation/geometry_comp_test_new_v1_v2-1/comparedTracker_my_misalined_vs_my_IDEAL.root=my_misalined|4|1")'
    mv result.root GeometryComparison.Tracker_result.root
    cmsStage -f GeometryComparison.Tracker_result.root /store/caf/user/$USER/AlignmentValidation/geometry_comp_test_new_v1_v2-1
else
    echo "GeometryComparison.Tracker_result.root is up-to-date, no need to compare again."
    cmsStage -f /store/caf/user/$USER/AlignmentValidation/geometry_comp_test_new_v1_v2-1/GeometryComparison.Tracker_result.root .
fi





# clean-up
# ls -l *.root
rm -f *.root

#zip stdout and stderr from the farm jobs
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/data/commonValidation/CMSSW_7_4_1/src/Alignment/OfflineValidation/test/forAPE/geometry_comp_test_new_v1_v2-1
find . -name "*.stderr" -exec gzip -f {} \;
find . -name "*.stdout" -exec gzip -f {} \;
