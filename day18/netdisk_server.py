# 作者: 王道 龙哥
# 2023年03月08日11时16分28秒
from socket import *
import struct
import os


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.path = '.'
        self.tcp_server_socket: socket = None
        self.new_socket: socket = None

    def tcp_init(self):
        tcp_server_socket = socket(AF_INET, SOCK_STREAM)
        # 重用对应地址和端口
        tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 本地IP地址和端口
        address = (self.ip, self.port)

        tcp_server_socket.bind(address)
        # 端口激活
        tcp_server_socket.listen(100)
        self.tcp_server_socket = tcp_server_socket

    def send_train(self, data: str):
        data_bytes = data.encode('utf8')
        data_len = len(data_bytes)
        self.new_socket.send(struct.pack('I', data_len)
                             )  # 发火车头，4个字节，包含的是文件名的长度
        self.new_socket.send(data_bytes)  # 车厢是文件名

    def recv_train(self, new_socket):
        train_len = new_socket.recv(4)  # 拿到火车头
        train_content_len = struct.unpack('I', train_len)[0]
        train_content: bytes = new_socket.recv(train_content_len)
        return train_content.decode('utf8')

    def do_ls(self):
        """
        当前路径下的信息传输给客户端
        :return:
        """
        data = ''
        for file in os.listdir(self.path):
            data += file+' '*5+str(os.stat(file).st_size)+'\n'
        self.send_train(data)

    def deal_command(self):
        new_socket, new_addr = self.tcp_server_socket.accept()
        self.new_socket = new_socket
        print(new_addr)
        while True:
            # 接收客户端发过来的命令
            command = self.recv_train(new_socket)
            if command[:2] == 'ls':
                self.do_ls()
            elif command[:2] == 'cd':
                self.do_cd(command)
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:2] == 'rm':
                self.do_rm(command)
            elif command[:4] == 'gets':
                self.do_gets(command)
            elif command[:4] == 'puts':
                self.do_puts(command)
            else:
                print('wrong command')


if __name__ == '__main__':
    s = Server('192.168.157.130', 2000)
    s.tcp_init()
    s.deal_command()
