import socket
import sys

messages = [
    'This is the message. ',
    'It will be sent ',
    'in parts.',
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

for message in messages:
    outgoing_data = message.encode()

    # 让每个套接字都发送消息。
    for s in socks:
        print('{}: sending {!r}'.format(s.getsockname(),
                                        outgoing_data),
              file=sys.stderr)
        s.send(outgoing_data)

    # 让每个套接字都读取响应。
    for s in socks:
        data = s.recv(1024)
        print('{}: received {!r}'.format(s.getsockname(),
                                         data),
              file=sys.stderr)
        if not data:
            print('closing socket', s.getsockname(),
                  file=sys.stderr)
            s.close()