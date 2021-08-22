# coding=utf-8
import platform
global sysVer
LINUX = 0
WINDOWS = 1
MACOS = 2
UNIX = 3
operSys = platform.system().lower()
if operSys == ("windows".lower()):
    sysVer = WINDOWS
elif operSys == ("linux".lower()):
    sysVer = LINUX
elif operSys == ("mac os".lower()):
    sysVer = MACOS


import socket
hostname = socket.gethostname()
ipAddr = socket.gethostbyname(hostname)


def isLocal(ip):
    isL = False
    if (ip is None or ip == 'localhost'
            or ip == '127.0.0.1' or ip == ipAddr):
        isL = True
    return isL

X_CORE_CONFIG = 'XCORE'
DEFAULT_LOG_NAME = 'xcore.log'


RESULT_SUCCESS = 1
RESULT_FAIL = 0
