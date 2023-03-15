#!/usr/bin/env python3
#coding:utf-8
#代码5-9 s chat_01s.py 
import socketserver
class Chat_server(socketserver.StreamRequestHandler):
    # SRH支持TCP
    def handle(self):
        conn=self.request # request表示的与客户端的连接实例对象值
        try:
            while True:
                data_b=conn.recv(1024)
                print('data_b=', data_b)
                if conns.count(conn)==0: # 若不存在，则表示是新接收的客户端
                    conns.append(conn)
                    name_s = data_b.decode('utf-8')
                    users.setdefault(conn,name_s) # 给字典users添加键值对
                    data_s = ''
                    data = 'Welcome '+name_s+'!'
                else:
                    name_s = users.get(conn)
                    data_s = data_b.decode('utf-8')
                    data = name_s+':'+data_s 
                print('data=', data)
                data_b=data.encode('utf-8')
                for cn in conns:
                    cn.send(data_b)
                if data_s.upper()[0:3]=='BYE':
                    print('%s is exited!' % name_s)
                    conns.remove(conn)
                    del(users[conn])
                    break
        except Exception as e:
            print('Error is',e)

conns = [] # 列表变量conns，存储与客户端的连接对象conn
users = {} # 第34行定义字典变量users，字典的键为conn，值为name_s
ip='192.168.157.130'
server = socketserver.ThreadingTCPServer((ip,9988),Chat_server)
print('Wait for TCP connecting...')
server.serve_forever() # 以无限循环形式处理客户端请求。