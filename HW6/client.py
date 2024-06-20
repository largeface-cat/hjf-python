import socket
import sys
import time

messages = [
    'Zhang San',
    'Xiao Ming',
    'Hello everybody!',
]
server_address = ('localhost', 9999)

# 创建 TCP/IP 套接字
socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

# 连接服务器所监听的套接字端口。
print('connecting to {} port {}'.format(*server_address),
      file=sys.stderr)
for s in socks:
    s.connect(server_address)

socks[0].send(messages[0].encode('utf-8'))
socks[1].send(messages[0].encode('utf-8'))
data = socks[0].recv(1024).decode('utf-8')
print(data,end='to {} \n'.format(socks[0].getsockname()[1]))
if not data:
    print('sock 0 end!')
    socks[0].close()
data = socks[1].recv(1024).decode('utf-8')
print(data,end='to {} \n'.format(socks[1].getsockname()[1]))
if not data:
    print('sock 1 end!')
    socks[1].close()
socks[1].send(messages[1].encode('utf-8'))
data = socks[1].recv(1024).decode('utf-8')
print(data,end='to {} \n'.format(socks[1].getsockname()[1]))
if not data:
    print('sock 1 end!')
    socks[1].close()
socks[0].send(messages[2].encode('utf-8'))
data = socks[1].recv(1024).decode('utf-8')
print(data,end='to {} \n'.format(socks[1].getsockname()[1]))
if not data:
    print('sock 1 end!')
    socks[1].close()

