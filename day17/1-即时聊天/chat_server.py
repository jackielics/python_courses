# 作者: 王道 龙哥
# 2023年03月07日11时24分09秒
from socket import *
import select
import sys

# 1 初始化一个套接字
tcp_server_socket = socket(AF_INET, SOCK_STREAM)

#重用对应地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 2 bind
tcp_server_socket.bind(('', 2000))
# 3 listen 端口激活了
tcp_server_socket.listen(10)

client_socket, client_addr = tcp_server_socket.accept()
print(f'{client_addr}连上了')

epoll = select.epoll()
# 让epoll小兵帮我们监控标准输入
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
# 让epoll帮我们监控client_socket
epoll.register(client_socket.fileno(), select.EPOLLIN)

while True:
    # -1永久等待，轮询注册的事件集合，返回值为[(文件句柄，对应的事件)，(...),....]
    events = epoll.poll(-1, 2)
    for event in events:
        if event[0] == sys.stdin.fileno(): #代表标准输入缓冲区可读了
            input_data = input()  # 这里会阻塞
            client_socket.send(input_data.encode('utf8'))
        elif event[0] == client_socket.fileno(): #代表client_socket接收缓冲区可读了
            recv_data = client_socket.recv(1000)
            if recv_data:
                print(recv_data.decode('utf8'))
            else: #如果没有从缓冲区读到数据，就是对端断开了
                print('byebye')
                client_socket.close()
                tcp_server_socket.close()
                exit(0)
