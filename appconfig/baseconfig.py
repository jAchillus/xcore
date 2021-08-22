# encoding=utf-8
import logging
import os
from xcore.appconfig import SysConst


def logGlobalSet(glevel=logging.INFO, gfilename=SysConst.DEFAULT_LOG_NAME):
    if glevel is None:
        global defualtLevel
        glevel = defualtLevel + 10
    logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=glevel,
                        filename=gfilename, filemode="a")
    pass

global configJson
configJson = {}


def parseProperties(file):
    global configJson
    with open(file, 'r', encoding='utf-8') as data:

        for line in data:

            if line is None or line == '':
                continue

            if line.startswith('#'):
                continue
            lineArr = line.split("=")
            if len(lineArr) == 2:
                configJson[lineArr[0].replace(" ", "").replace("\n", "")] = lineArr[1].replace(" ", "").replace("\n", "")


def getConfigValue(key):
    global configJson
    return configJson.get(key)

sysParams = os.environ


def getConfigHome():
    return sysParams.get(SysConst.X_CORE_CONFIG)


def loadConfig(config):
    if not os.path.isdir(config):
        return
    for path in os.listdir(config):
        fil = config + "/" + path
        if os.path.isdir(fil) and path == "log":
            continue
        elif os.path.isdir(fil):
            loadConfig(fil)
        elif not path.endswith('.log'):
            parseProperties(fil)

global logPath
global configPath
global logName
global defualtLevel
logName = None


def loadLogConfig():
    global logPath
    global configPath
    global logName
    global defualtLevel
    logPath = getConfigValue("LOG_PATH")
    defualtLevel = getConfigValue("LOG_LEVEL")
    if defualtLevel is None:
        defualtLevel = logging.INFO
    configPath = getConfigHome()
    if logPath is None or logPath == '':
        logPath = ''
        if configPath is not None:
            logPath = configPath + "/log/"

    logName = getConfigValue("LOG_NAME")
    if logName is None:
        logName = logPath + "/" + SysConst.DEFAULT_LOG_NAME

    pass

global refreshCache
refreshCache = False


def load(config=''):
    global refreshCache
    if refreshCache:
        return
    os.environ[SysConst.X_CORE_CONFIG] = config
    loadConfig(config)
    loadLogConfig()
    logGlobalSet(defualtLevel, logName + 'thrid')
    refreshCache = True
    pass
