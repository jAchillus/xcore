# coding=utf-8


def fillupSpace(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


def encryptByDes(text):

    textTmp = fillupSpace(text)
    encryptedStr = des.encrypt(textTmp.encode('utf-8'))  # 加密
    return encryptedStr


def decryptByDes(text):

    textTmp = fillupSpace(text)
    decryptDecryptStr = des.decrypt(textTmp).decode().rstrip(' ')
    return decryptDecryptStr

import base64


def encryptBybase64(text):
    return text  # base64.encodestring(text.encode()).decode()


def decryptBybase64(text):
    return text  # base64.decodestring(text.encode()).decode()
