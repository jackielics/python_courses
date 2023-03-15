#!/usr/bin/env python3
#coding:utf-8
from socket import *
import select
import sys
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
# if len(sys.argv) !=2:
#     print('./chat_client.py IP')
#     exit(2)
# # 本地IP 地址和端口
# address = (sys.argv[1], 2000)
address = ('192.168.157.130', 2000)

name = input("请输入你的名字：")
# 连接服务器
tcp_client_socket.connect(address)
epoll = select.epoll()
epoll.register(tcp_client_socket.fileno(), select.EPOLLIN)
epoll.register(sys.stdin.fileno(), select.EPOLLIN)
print("请在空格处输入你要发送的内容：")
while True:
    epoll_list = epoll.poll()
    for fd, event in epoll_list:
        if fd == sys.stdin.fileno():
            try:#这里主要是ctrl+D 后我们能够自己控制退出码
                input_data = input()
            except:
                print('I want go')
                exit(2)
            finally:
                input_data =name +":"+input_data
                tcp_client_socket.send(input_data.encode('utf-8'))
        if fd == tcp_client_socket.fileno():
            recv_data = tcp_client_socket.recv(1024)
            if not recv_data:
                exit(0)
            print(recv_data.decode('utf-8'))
tcp_client_socket.close()
