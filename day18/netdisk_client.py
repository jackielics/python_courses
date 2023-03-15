# 作者: 王道 龙哥
# 2023年03月08日11时16分45秒

from socket import *
import struct


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client_socket = None

    def tcp_connect(self):
        tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        # 本地IP地址和端口
        address = (self.ip, self.port)
        # 连接服务器
        tcp_client_socket.connect(address)
        self.client_socket = tcp_client_socket

    def send_train(self, new_socket, data: str):

        data_bytes = data.encode('utf8')
        data_len = len(data_bytes)
        # 将数据按照指定的格式转换为二进制数据（即打包）
        new_socket.send(struct.pack('I', data_len))  # 发火车头，4个字节，包含的是文件名的长度
        new_socket.send(data_bytes)  # 车厢是文件名

    def recv_train(self, new_socket):
        train_len = new_socket.recv(4)  # 拿到火车头
        train_content_len = struct.unpack('I', train_len)[0]
        train_content: bytes = new_socket.recv(train_content_len)
        return train_content.decode('utf8')

    def user_operation(self):
        while True:
            command = input("\n请输入命令:\t")
            # 发给服务器
            self.send_train(self.client_socket, command)
            data = self.recv_train(self.client_socket)
            print(data, end='')


if __name__ == '__main__':
    c = Client('192.168.157.130', 2000)
    c.tcp_connect()
    c.user_operation()
