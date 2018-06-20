import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8080))
while True:
    msg = input('>>>')
    if msg == 'bye':
        sk.send(b'bye')
        break
    sk.send(msg.encode('utf-8'))
    ret = sk.recv(1024).decode('utf-8')
    if ret == 'bye':break
    print(ret)
sk.close()