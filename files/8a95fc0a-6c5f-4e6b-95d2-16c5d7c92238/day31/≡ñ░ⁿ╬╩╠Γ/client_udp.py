import socket
import subprocess
sk = socket.socket(type=socket.SOCK_DGRAM)
addr = ('127.0.0.1',8090)
sk.sendto('吃了么'.encode('utf-8'),addr)
while True:
    cmd,addr = sk.recvfrom(10000)
    ret = subprocess.Popen(cmd.decode('gbk'),shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    std_out = 'stdout :'+(ret.stdout.read()).decode('gbk')
    std_err = 'stderr :'+(ret.stderr.read()).decode('gbk')
    print(std_out)
    print(std_err)
    sk.sendto(std_out.encode('utf-8'),addr)
    sk.sendto(std_err.encode('utf-8'),addr)
sk.close()



# 网盘
# 文件的 上传  下载

# server端 和 client端
# 登录   客户端登录 将用户名和密码发给服务端 服务端确认信息之后
# 上传下载
# 选择上传 / 下载
# 上传 ：选择要上传的文件路径，在server创建一个同名的空文件.cache
# 下载:  选择要下载的文件路径，在client端创建一个同名的空文件















