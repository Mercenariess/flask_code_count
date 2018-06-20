# 通过一个例子 来认识网络编程中一个重要的概念
# 所有的客户端执行 server 端 下发的指令
# 将结果反馈回来，我来接收

# ret = os.popen()

import subprocess
res = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE,stderr= subprocess.PIPE)
print('stdout :',res.stdout.read().decode('gbk'))
print('stderr :',res.stderr.read().decode('gbk'))