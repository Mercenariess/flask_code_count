# 提供服务
# 接收信息 时间的格式
# 将我的时间转换成 接受到的格式
# 发回给客户端
import time
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',8090))
while True:
    strf,addr = sk.recvfrom(1024)
    strf = strf.decode('utf-8')
    res = time.strftime(strf).encode('utf-8')
    sk.sendto(res,addr)
sk.close()