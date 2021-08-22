# coding=utf-8
import socket
import logging
from xcore.log import Log
logger = Log.getLogger(name='network')


def netIsUsed(port, ip='127.0.0.1'):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        logger.info('%s:%d is used' % (ip, port))
        return True
    except:
        logger.info('%s:%d is unused' % (ip, port))
        return False
