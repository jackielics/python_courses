#!/usr/bin/env python3
# coding:utf-8
from socket import *
import select
import sys
tcp_server_socket = socket(AF_INET, SOCK_STREAM)
# 重用对应地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 本地IP 地址和端口
address = ('192.168.157.130', 2000)
tcp_server_socket.bind(address)
# 端口激活
tcp_server_socket.listen(100)
# # 创建一个epoll 对象
epoll = select.epoll()
epoll.register(tcp_server_socket.fileno(), select.EPOLLIN)
# 存放聊天室每个用户的client_socket 信息
client_list = []
while True:
    epoll_list = epoll.poll()
    for fd, event in epoll_list:
        if fd == tcp_server_socket.fileno():
            client_socket, clientAddr = tcp_server_socket.accept()
            # 每个连接上的用户添加到列表中，同时把它注册了
            print("{} is coming".format(clientAddr))
            client_list.append(client_socket)
            epoll.register(client_socket.fileno(), select.EPOLLIN)
        for client in client_list:
            if fd == client.fileno():
                # 读取client 的数据，群发给其他人,没数据代表断开，有数据发给其他人
                recv_data = client.recv(1024)
                if not recv_data:
                    epoll.unregister(client.fileno())
                    client_list.remove(client)
                    client.close()
                else:
                    for other_client in client_list:
                        if other_client is not client:
                            other_client.send(recv_data)
client_socket.close()
tcp_server_socket.close()
