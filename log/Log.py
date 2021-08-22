# coding=utf-8
import logging
from xcore.appconfig import baseconfig
from xcore.appconfig import SysConst
from xcore import ConfigurationMgr


def getLogger(name, fileName=None):
    logger = logging.getLogger(name)
    level = ConfigurationMgr.getConfigValue('log.' + name, baseconfig.defualtLevel)

    logger.setLevel(level)
    if fileName is not None:
        fileName = baseconfig.logPath + "/" + fileName
    elif baseconfig.logName is not None:
        fileName = baseconfig.logName
    #print("log=%s,%s" % (name, fileName))
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(format)

    fh = logging.FileHandler(fileName, mode='a')
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    cons = ConfigurationMgr.getConfigValue('IS_CONSOLE', 'N')
    if cons == 'Y':
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
