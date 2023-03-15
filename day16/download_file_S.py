#!/usr/bin/env python3
#代码4-3 s socket03s.py
#coding:utf-8
import socket
import os
def sendfile(conn):
    '''
    自定义函数sendfile()，用于处理客户端请求，主要实现向客户端发送文件数据。
    '''
    str1 = conn.recv(1024)
    filename = str1.decode('utf-8')
    print('The client requests my file:',filename)
    if os.path.exists(filename):
        print('I have %s,begin to download!' % filename)
        conn.send(b'yes') # bytes格式的'yes'，先send一个提示
        conn.recv(1024)
        size=1024
        with open(filename,'rb')as f:
            while True:
                data=f.read(size)
                conn.send(data)
                if len(data)<size:
                    # 每次数据发送结束，都判断该次数据是否小于size，
                    # 如果小于size，则表示已经到达文件末尾，该次数据为文件最后数据，
                    break
        print('%s is downloaded successfully!'%filename)
    else:
        print('Sorry,I have no %s!' % filename)
        conn.send(b'no')
    conn.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.157.130',8088))
s.listen(1)
print('Wait for connecting...')
while True:
    (conn,addr)=s.accept()
    sendfile(conn)