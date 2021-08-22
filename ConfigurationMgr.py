# coding=utf-8
import os
from xcore.appconfig import baseconfig
from xcore.appconfig import SysConst
sysParams = os.environ
configPath = "D:\\DevelopTools\\Projects\\autoUpgrade\\autoupgrade\\config"
if SysConst.X_CORE_CONFIG in sysParams:
    configPath = sysParams[SysConst.X_CORE_CONFIG]

baseconfig.load(configPath)


def getConfigValue(key):
    return baseconfig.getConfigValue(key)


def getConfigValue(key, default=None):
    value = baseconfig.getConfigValue(key)
    if value is None:
        value = default
    return value
