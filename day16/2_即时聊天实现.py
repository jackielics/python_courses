#!/usr/bin/python3
from socket import *
import select
import sys
tcp_server_socket = socket(AF_INET, SOCK_STREAM)
#重用对应地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 本地IP 地址和端口
address = ('192.168.1.111', 2000)
tcp_server_socket.bind(address)
# 端口激活
tcp_server_socket.listen(100)
client_socket, clientAddr = tcp_server_socket.accept()
print(clientAddr)
# print(tcp_server_socket.fileno())
# print(client_socket.fileno())
# # 创建一个epoll 对象
epoll = select.epoll()
epoll.register(client_socket.fileno(), select.EPOLLIN)
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
while True:
    epoll_list = epoll.poll()
    for fd, event in epoll_list:
        if fd == sys.stdin.fileno():
            input_data = input()
            if not input_data:
                print('I want go')
                exit(1)
            client_socket.send(input_data.encode('utf-8'))
        if fd == client_socket.fileno() and event == select.EPOLLIN:
            recv_data = client_socket.recv(1024)
            if not recv_data:#通过判断recv_data 来判断对方是否断开
                print('byebye')
                exit(0) #紧张
            print(recv_data.decode('utf-8'))
client_socket.close()
tcp_server_socket.close()