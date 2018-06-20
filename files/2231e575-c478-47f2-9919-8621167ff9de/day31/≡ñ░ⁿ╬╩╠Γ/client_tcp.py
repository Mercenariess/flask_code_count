# 在client端接收命令并执行

import socket
import subprocess
sk = socket.socket()
sk.connect(('127.0.0.1',8090))
while True:
    cmd = sk.recv(1024).decode('gbk')
    ret = subprocess.Popen(cmd,shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    std_out = 'stdout :'+(ret.stdout.read()).decode('gbk')
    std_err = 'stderr :'+(ret.stderr.read()).decode('gbk')
    print(std_out)
    print(std_err)
    sk.send(std_out.encode('utf-8'))
    sk.send(std_err.encode('utf-8'))
sk.close()

# 数据已经乱了
# send recv
# send recv
#       recv   没有接收完
#接收多了
# 黏包现象
# 不丢包