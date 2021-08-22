# coding=utf-8
import paramiko


class SSHObj(object):

    """docstring for SSHObj"""
    ssh = None

    def __init__(self):
        super(SSHObj, self).__init__()

    # def __init__(self, host, port, user, password):
    #     super(SSHObj, self).__init__()
    #     self.setSshCconnect(host, port, user, password)

    def __init__(self, hostInfo):
        super(SSHObj, self).__init__()
        self.setSshCconnect(hostInfo['host'], hostInfo['port'], hostInfo['user'], hostInfo['password'])

    def setSshCconnect(self, host, port, user, password):
        # SSH远程连接
        self.ssh = paramiko.SSHClient()  # 创建sshclient
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
        self.ssh.connect(host, port, user, password)

    def execSSHCommand(self, command, encode='utf-8'):
        # 执行命令并获取执行结果
        stdin, stdout, stderr = self.ssh.exec_command('source ~/.bash_profile;' + command)
        out = stdout.read().decode(encode)
        err = stderr.read().decode(encode)
        return out, err

    def close(self):
        self.ssh.close()
        pass
