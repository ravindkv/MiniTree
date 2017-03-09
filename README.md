# MiniTree

(1): SET UP THE CMSSSW

cmsrel CMSSW_8_0_25
cd CMSSW_8_0_25/src/
cmsenv

(2): DOWNLOAD THIS PACKAGE

git clone https://github.com/ravindkv/MiniTree.git

(3): RUN THE CODES

cd MiniTree 
scram b -j20
cd Selection/test
cmsRun muons_miniAOD_to_ntuple_13TeV_cfg.py

