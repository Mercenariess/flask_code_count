import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8080)

sk.sendto(b'hello',ip_port)
ret,addr = sk.recvfrom(1024)
print(ret.decode('utf-8'))

sk.close()

# client端不需要connect 因为UDP协议是不需要建立连接的
# 直接了解到对方的ip和端口信息就发送数据就行了
# sendto和recvfrom的使用方法是完全和server端一致的