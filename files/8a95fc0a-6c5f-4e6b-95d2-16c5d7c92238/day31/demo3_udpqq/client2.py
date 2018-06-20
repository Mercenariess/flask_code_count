import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8080)
while True:
    info = input('二哥 ：')
    info = ('\033[32m来自二哥的消息 ：%s\033[0m'%info).encode('utf-8')
    sk.sendto(info,ip_port)
    msg,addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))

sk.close()