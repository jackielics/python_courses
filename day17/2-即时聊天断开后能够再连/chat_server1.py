# 作者: 王道 龙哥
# 2023年03月07日11时24分09秒
from socket import *
import select
import sys

def chat_server():
    # 1 初始化一个套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    #重用对应地址和端口
    tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # 1表示开启重用
    """ 使用setsockopt()函数设置SO_REUSEADDR选项为1，可以使该服务器程序的端口被关闭后立即释放，
    以便其他进程可以立即使用该端口。如果没有设置该选项，关闭服务器程序后，该端口会在一段时间内
    （通常为几分钟）处于TIME_WAIT状态，此时其他进程无法使用该端口，从而导致端口资源的浪费。 """
    # 2 bind
    tcp_server_socket.bind(('', 2000))
    # 3 listen 端口激活了
    tcp_server_socket.listen(10)

    epoll = select.epoll()
    epoll.register(sys.stdin.fileno(), select.EPOLLIN) # 标准输入用于接收用户输入
    epoll.register(tcp_server_socket.fileno(), select.EPOLLIN) # tcp_server_socket用于接收客户端的连接请求

    while True:
        # -1永久等待，轮询注册的事件集合，返回值为[(文件句柄，对应的事件)，(...),....]
        events = epoll.poll(-1)
        for event in events:
            if event[0]==tcp_server_socket.fileno():
                client_socket, client_addr = tcp_server_socket.accept()
                print(f'{client_addr}连上了')
                #加入监听
                epoll.register(client_socket.fileno(),select.EPOLLIN)
            elif event[0] == sys.stdin.fileno(): # 代表标准输入缓冲区可读了
                input_data = input()  # 这里会阻塞
                client_socket.send(input_data.encode('utf8'))
            elif event[0] == client_socket.fileno(): # 代表client_socket接收缓冲区可读了
                recv_data = client_socket.recv(1000)
                if recv_data:
                    print(recv_data.decode('utf8'))
                else: #如果没有从缓冲区读到数据，就是对端断开了
                    print('客户端断开了')
                    #解除注册
                    epoll.unregister(client_socket.fileno())
                    client_socket.close()
                    break

if __name__ == '__main__':
    chat_server()
