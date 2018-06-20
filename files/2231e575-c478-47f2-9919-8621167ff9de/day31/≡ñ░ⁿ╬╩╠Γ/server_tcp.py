# 基于tcp实现远程执行命令
# 在server端下发命令

import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8090))
sk.listen()

conn,addr = sk.accept()
while True:
    cmd = input('>>>')
    conn.send(cmd.encode('utf-8'))
    ret = conn.recv(1024).decode('utf-8')
    print(ret)

conn.close()
sk.close()