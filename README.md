# MiniTree

#### Set the CMSSSW release ####

* cmsrel CMSSW_8_0_28
* cd CMSSW_8_0_28/src/
* cmsenv

#### Download the MiniTree package ####

* git clone https://github.com/ravindkv/MiniTree.git

#### Compile and Run the codes ####

* cd MiniTree/Selection/ 
* scram b -j 20
* cd test
* cmsRun muonMiniTreeMaker_cfg.py

