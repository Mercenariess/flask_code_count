import socket
sk = socket.socket(type=socket.SOCK_DGRAM)  #DGRAM datagram
sk.bind(('127.0.0.1',8080))       #只有服务端有的

msg,addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
sk.sendto(b'bye',addr)

sk.close()


# udp的server 不需要进行监听也不需要建立连接
# 在启动服务之后只能被动的等待客户端发送消息过来
# 客户端发送消息的同时还会 自带地址信息
# 消息回复的时候 不仅需要发送消息，还需要把对方的地址填写上











