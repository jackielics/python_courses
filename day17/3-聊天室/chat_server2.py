# 作者: 王道 龙哥
# 2023年03月07日11时24分09秒
from socket import *
import select
import sys


def chat_server():
    # 1 初始化一个套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    # 重用对应地址和端口
    tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 2 bind
    tcp_server_socket.bind(('', 2000))
    # 3 listen 端口激活了
    tcp_server_socket.listen(10)

    epoll = select.epoll()
    # 让epoll小兵帮我们监控标准输入
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    # 让epoll帮我们监控tcp_server_socket
    epoll.register(tcp_server_socket.fileno(), select.EPOLLIN)
    client_dict = {}
    while True:
        # -1永久等待，轮询注册的事件集合，返回值为[(文件句柄，对应的事件)，(...),....]
        events = epoll.poll(-1)
        for event in events:
            if event[0] == tcp_server_socket.fileno():
                client_socket, client_addr = tcp_server_socket.accept()
                print(f'{client_addr}连上了')
                # 加入监听
                epoll.register(client_socket.fileno(), select.EPOLLIN)
                # 放入字典
                client_dict[client_socket.fileno()] = client_socket
            else:
                recv_data = client_dict[event[0]].recv(1000)
                if recv_data:
                    # 群发给其他客户端
                    for client in client_dict.items():
                        if client[0] != event[0]:
                            client[1].send(recv_data)
                else:  # 如果没有从缓冲区读到数据，就是对端断开了
                    print('有客户端断开了')
                    # 解除和客户端对应的socket的注册
                    epoll.unregister(event[0])
                    client_dict[event[0]].close()
                    del client_dict[event[0]]
                    break


if __name__ == '__main__':
    chat_server()
