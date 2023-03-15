#!/usr/bin/env python3
#coding:utf-8
#代码4-2 s socket02s.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('192.168.157.130', 8088)) # 将对象s绑定到元组地址上
s.bind(('192.168.80.1', 8088)) # 将对象s绑定到元组地址上
s.listen(1) # 开始监听来自客户端的1x连接
print('Wait for connecting...')
(conn, addr) = s.accept() # 接受一个来自客户端的连接
print('conn=', conn)
print('addr =', addr)
while True:
    str1 = conn.recv(1024) # 一次最多接收1024B数据
    str2 = str(str1, encoding='utf-8') # 将bytes字节流数据转换为字符串
    print('I received a string is:', str2)
    str3 = str2.upper()
    conn.send(str3.encode('utf-8')) # conn的发送方式
    if str2=='.': # 自定义结束符
        break
conn.close() # 断开连接
s.close() # 释放对象s