import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
addr = ('127.0.0.1',8090)
info = input('>>>').encode('utf-8')
sk.sendto(info,addr)
ret,addr = sk.recvfrom(1024)
print(ret.decode('utf-8'))

sk.close()