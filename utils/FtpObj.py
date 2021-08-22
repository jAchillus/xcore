# coding=utf-8
import paramiko
import logging
from xcore.log import Log


class FtpObj(object):

    """整理公共方便使用的ftp工具"""

    host = None
    port = None
    pwd = None
    user = None
    sf = None
    sftp = None
    logger = Log.getLogger("ftp")

    def __init__(self, arg):
        super(FTPObj, self).__init__()
        self.arg = arg

    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.sf = paramiko.Transport((host, port))
        self.sf.connect(username=user, password=pwd)
        self.sftp = paramiko.SFTPClient.from_transport(self.sf)

    def __init__(self, hostInfo):
        self.logger.info('hostInfo:%s' % hostInfo)
        self.host = hostInfo['host']
        self.port = int(hostInfo['port'])
        self.user = hostInfo['user']
        self.pwd = hostInfo['pwd']
        self.sf = paramiko.Transport((self.host, self.port))
        self.sf.connect(username=self.user, password=self.pwd)
        self.sftp = paramiko.SFTPClient.from_transport(self.sf)

    def sftpDownload(self, remotePath, localPath):
        logging.info("localPath:%s" % localPath)
        # self.sftp.chdir(remotePath)
        # logger.info(sftp.stat(remote))
        self.sftp.get(remotePath, localPath)

    def sftpUpload(self, localPath, remotePath):
        logging.info("localPath:%s" % localPath)
        # logger.info(sftp.listdir())
        # self.sftp.chdir(remotePath)
        # logger.info(sftp.stat(remote))
        self.sftp.put(localPath, remotePath)

    def sftpListFile(self, remotePath):
        logging.info("remotePath:%s" % remotePath)

        return self.sftp.listdir(remotePath)

    def closeFtp(self):
        self.sf.close()

import ftplib


def ftpCopy():
    ftp = ftplib.FTP()
    ftp.set_debuglevel(1)  # 不开启调试模式
    ftp.connect(host='10.21.17.163', port=22)  # 连接ftp
    ftp.login('zdj', 'zdj')  # 登录ftp
    ftp.set_pasv(False)

    logger.info(ftp.getwelcome())  # 显示登录ftp信息
    file_list = ftp.nlst(ftp_file_path)
    logger.debug
    for file_name in file_list:
        logger.info("file_name"+file_name)
        ftp_file = os.path.join(ftp_file_path, file_name)
        logger.info("ftp_file:"+ftp_file)
        #write_file = os.path.join(dst_file_path, file_name)
        write_file = "D://tmp"+file_name  # 在这里如果使用os.path.join 进行拼接的话 会丢失dst_file_path路径,与上面的拼接路径不一样
        logger.info("write_file"+write_file)
        if file_name.find('.png') > -1 and not os.path.exists(write_file):
            logger.info("file_name:"+file_name)
            #ftp_file = os.path.join(ftp_file_path, file_name)
            #write_file = os.path.join(dst_file_path, file_name)
            # with open(write_file, "wb") as f:
            # ftp.retrbinary('RETR %s' % ftp_file, f.write, buffer_size)
        # f.close()

    ftp.quit()
    pass
