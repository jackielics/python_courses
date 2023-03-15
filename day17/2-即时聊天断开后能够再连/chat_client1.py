# 作者: 王道 龙哥
# 2023年03月07日11时29分11秒
from socket import *
import select
import sys

if len(sys.argv) != 2:
    print('error args')
    exit(-1)

# 1 初始化一个套接字
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
dest_addr = (sys.argv[1], 2000)
# 2 连接服务器端，连接不上报异常
tcp_client_socket.connect(dest_addr)

epoll = select.epoll() # 创建epoll对象

epoll.register(sys.stdin.fileno(), select.EPOLLIN) # 注册标准输入

epoll.register(tcp_client_socket.fileno(), select.EPOLLIN) # 注册client_socket

while True:
    # -1永久等待，轮询注册的事件集合，返回值为[(文件句柄，对应的事件)，(...),....]
    events = epoll.poll(-1, 2) # -1永久等待, 2表示最多返回的事件数
    for event in events:
        if event[0] == tcp_client_socket.fileno(): # 代表client_socket接收缓冲区可读了
            recv_data = tcp_client_socket.recv(1000)
            if recv_data:
                print(recv_data.decode('utf8'))
            else:  # 如果没有从缓冲区读到数据，就是对端断开了
                print('byebye')
                tcp_client_socket.close()
                exit(0)
        elif event[0] == sys.stdin.fileno(): # 代表标准输入缓冲区可读了
            input_data = input()
            tcp_client_socket.send(input_data.encode('utf8'))
