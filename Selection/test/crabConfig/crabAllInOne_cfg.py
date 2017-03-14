import FWCore.ParameterSet.Config as cms
from allMCsamples import allMCsamplesDict
from allDATAsamples import allDATAsamplesDict
import datetime

print len(allMCsamplesDict)

#Get nth key, value of MC sample
def getMCsampleValue(MCdict, n):
    return MCdict[list(MCdict)[n]]

def getMCsampleKey(MCdict, n):
   Value = getMCsampleValue(MCdict, n)
   todayDate = datetime.date.today()
   startingName = Value.split("/")[1].split("_")[0]
   Key = startingName+"_ntuple_"+str(todayDate)
   return Key

print getMCsampleKey(allMCsamplesDict, 10)
print getMCsampleValue(allMCsamplesDict, 10)

#Get nth key, value of DATA sample
def getDATAsampleValue(DATAdict, n):
    return DATAdict[list(DATAdict)[n]]

def getDATAsampleKey(DATAdict, n):
   Value = getDATAsampleValue(DATAdict, n)
   todayDate = datetime.date.today()
   startingName = Value.split("/")[1].split("_")[0]
   Key = startingName+"_ntuple_"+str(todayDate)
   return Key

print getDATAsampleKey(allDATAsamplesDict, 3)
print getDATAsampleValue(allDATAsamplesDict, 3)

#USER INPUTS
isMuons = True
isElectrons = False
isMC = True
isDATA = False
#rangeMC = len(allMCsamplesDict)
#rangeDATA = len(allDATAsamplesDict)
rangeMC = 1
rangeDATA = 1


#CRAB PARAMETERS
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'

#Muon channel
if isMuons:
    if isMC:
        for m in range(rangeMC):
            mu_MC = "_muons_MC"
            #dirName of the output Ntuples at T2
            config.General.requestName = getMCsampleKey(allMCsamplesDict, m) +mu_MC

            #local dirName of crab jobs
            config.General.workArea = 'crab_ntuple' +mu_MC

            #fileName of output Ntuples at T2 are taken form psetName, e.g process.TFileService.fileName
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'

            #specify the dataset. Comment process.source.fileNames in psetName
            config.Data.inputDataset = getMCsampleValue(allMCsamplesDict, m)

            #dir(/cms/store/user/rverma/) at T2
            config.Data.outLFNDirBase = '/store/user/%s/test/crab'mu_MC+'/'+getMCsampleKey(allMCsamplesDict, m)+mu_MC % (getUsernameFromSiteDB())

    if isDATA:
        for d in range(rangeDATA):
            mu_DATA = "_muons_DATA"
            config.General.requestName = getDATAsampleKey(allDATAsamplesDict, d) +mu_DATA
            config.General.workArea = 'crab_ntuple'+mu_DATA
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getDATAsampleValue(allDATAsamplesDict, d)
            config.Data.outLFNDirBase = '/store/user/%s/test/crab_ntuple'+mu_DATA+'/'+getDATAsampleKey(allMCsamplesDict, d)+mu_DATA % (getUsernameFromSiteDB())

#Electron channel
if isElectrons:
    if isMC:
        for m in range(rangeMC):
            ele_MC = "_electrons_MC"
            config.General.requestName = getMCsampleKey(allMCsamplesDict, m) +ele_MC
            config.General.workArea = 'crab_ntupe' +ele_MC
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getMCsampleValue(allMCsamplesDict, m)
            config.Data.outLFNDirBase = '/store/user/%s/test/crab_ntuple'+ele_MC+'/'+getMCsampleKey(allMCsamplesDict, m)+ele_MC %(getUsernameFromSiteDB())

    if isDATA:
        for d in range(rangeDATA):
            ele_DATA = "_electrons_DATA"
            config.General.requestName = getDATAsampleKey(allDATAsamplesDict, d) +ele_DATA
            config.General.workArea = 'crab_ntupe' +ele_DATA
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getDATAsampleValue(allDATAsamplesDict, d)
            config.Data.outLFNDirBase = '/store/user/%s/test/crab_ntuple'+ele_DATA+'/'+getDATAsampleKey(allMCsamplesDict, d)+ele_DATA %(getUsernameFromSiteDB())


