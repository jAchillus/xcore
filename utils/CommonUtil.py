# coding=utf-8
import os
import logging
import platform
from xcore import ConfigurationMgr
''' 自动递归创建路径'''


def mkdir(path):
    ''' 自动递归创建路径1'''
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False

import sys

from xcore.log import Log
logger = Log.getLogger('common')


'''
执行命令
'''

import subprocess


def execSys(execComm, path=None):
    sh = execComm
    if path is not None:
        sh = execComm + "/" + path
    shellInfo = subprocess.call(execComm)
    return shellInfo

import socket


''' stf操作'''

import sys
# sys.path.append('analogcommunication')
# import FtpObj
from xcore.utils.FtpObj import FtpObj

import uuid


def copyFtp2Ftp(sourceFtp, destFtp, sourceFtpPath, destFtpPath):
    '''没有目标时候就是下载到本地'''
    tmp = ConfigurationMgr.getConfigValue('tmpPath', '')
    tmp = tmp + '/' + str(uuid.uuid1()) + '.tmppa'
    if destFtp is None:
        tmp = destFtpPath
    sourceFtp.sftpDownload(sourceFtpPath, tmp)
    logger.info("copyFtp2Ftp download sucess")

    if destFtp is not None:
        logger.info("copyFtp2Ftp start update dest:%s" % (destFtpPath))
        destFtp.sftpUpload(tmp, destFtpPath)
        destFtp.closeFtp()
    sourceFtp.closeFtp()

    logger.info("copyFtp2Ftp sucess")
    return tmp

from xcore.utils import PasswordUtil


def showFtpFile(sourceInfo, path):
    # sourceInfo = {'host': '10.21.40.139', 'port': 22, 'user': 'jenkins', 'pwd': 'amVua2lucyFAIzRRV0VS'}
    sourceInfo['pwd'] = PasswordUtil.decryptBybase64(sourceInfo['pwd'])
    sourceFtp = FtpObj(sourceInfo)
    listTmp = sourceFtp.sftpListFile(path)
    return (sorted(listTmp))


from xcore.utils.SSHObj import SSHObj


def updateSql(hostInfo, sql):
    logger.info(sql)
    print(sql)
    ssh = None
    out = None
    err = None
    try:
        ssh = SSHObj(hostInfo)
        out, err = ssh.execSSHCommand(sql, "GB2312")
        logger.info("ssh exec out:%s" % out)
        if err is not None and err != '':
            logger.warn("ssh exec err:%s" % err)
        pass
    except Exception as e:
        logger.warn(e)
        raise e
        pass
    finally:
        if ssh is not None:
            ssh.close()
        pass
    return out, err


def execSSHCommand(hostInfo, command, encode='utf-8'):
    ssh = None
    result = None
    try:
        ssh = SSHObj(hostInfo)
        result = ssh.execSSHCommand(command, encode)
    except Exception as e:
        raise e
    finally:
        if ssh is not None:
            ssh.close()
        pass
    return result


def getVersionServerInfo():

    verFtp_host = ConfigurationMgr.getConfigValue('verFtp.host')
    verFtp_port = ConfigurationMgr.getConfigValue('verFtp.port')
    verFtp_user = ConfigurationMgr.getConfigValue('verFtp.user')
    verFtp_pwd = ConfigurationMgr.getConfigValue('verFtp.pwd')
    verFtp = {"host": verFtp_host, "port": verFtp_port, "user": verFtp_user, "pwd": verFtp_pwd}
    return verFtp


def getDestServerList():

    servers = ConfigurationMgr.getConfigValue('destServers')
    serverArr = servers.split(",")
    return serverArr

global destServerList
destServerList = {}


def getDestServerInfoList():
    global destServerList

    for x in range(1, 50):
        index = str(x)
        destFtp_host = ConfigurationMgr.getConfigValue('destFtp.host.' + index)
        if destFtp_host is None:
            break
        destFtp_host = ConfigurationMgr.getConfigValue('destFtp.host.' + index)
        destFtp_port = ConfigurationMgr.getConfigValue('destFtp.port.' + index)
        destFtp_user = ConfigurationMgr.getConfigValue('destFtp.user.' + index)
        destFtp_pwd = ConfigurationMgr.getConfigValue('destFtp.pwd.' + index)
        destFtp = {"host": destFtp_host, "port": destFtp_port, "user": destFtp_user, "pwd": destFtp_pwd, "index": index}
        destServerList[destFtp_host] = destFtp
    return destServerList
getDestServerInfoList()


def getDestServerInfo(name, host=''):
    if host == '':
        return ConfigurationMgr.getConfigValue(name)
    global destServerList
    dest = destServerList[host]
    if dest is None:
        return None
    index = dest['index']
    param = ConfigurationMgr.getConfigValue(name + "." + index)
    if param is None:
        param = ConfigurationMgr.getConfigValue(name)

    return param


def getConfigValueByindex():
    pass


def getEncode(ip):
    cod = 'utf-8'
    cod = getDestServerInfo('destFtp.code', ip)

    return cod
