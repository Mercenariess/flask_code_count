import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',8090))
msg,addr = sk.recvfrom(10240)
while True:
    cmd = input('>>>')
    if cmd == 'q':
        break
    sk.sendto(cmd.encode('utf-8'),addr)
    msg,addr = sk.recvfrom(10240)
    print(msg.decode('utf-8'))

sk.close()


# udp
# udp 不会黏包
# udp 会丢包