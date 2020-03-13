## MiniTree Production For 2016 Excited Lepton Analysis

#### Set the CMSSSW release ####

* export SCRAM_ARCH=slc7_amd64_gcc700
* cmsrel CMSSW_10_4_0
* cd CMSSW_10_4_0/src/
* cmsenv

#### Download the MiniTree package ####

* git clone -b ExLep2016Tree git@github.com:ravindkv/MiniTree.git

#### Compile and Run the codes ####

* cd MiniTree 
* scram b -j 20
* cd Selection/test
* cmsRun produceTree_cfg.py 

#### Push the changes to github ####
* git branch
* git status
* git add -A
* git commit -m "new changes"
* git push origin ExLep2016Tree

