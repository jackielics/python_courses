#! /usr/bin/python3
# author claude


from socket import *
import struct
import os
from multiprocessing import Pool


def server_ls(client_socket):
    ls_list = os.listdir('.')  # 获取当前目录下的所有文件和目录
    ls_dict = {}
    for file_or_dir in ls_list:
        size = os.path.getsize(file_or_dir)  # 获取文件或目录的大小
        bool_type = os.path.isdir(file_or_dir)  # 判断是文件还是目录
        if bool_type:
            type = 'dir'  # 如果是目录，则type为'dir'
        else:
            type = 'file'  # 如果是文件，则type为'file'
        ls_dict[file_or_dir] = (type, size)  # 将文件或目录的类型和大小加入字典

    bytes_str_ls_dict = str(ls_dict).encode('utf-8')  # 将字典转换为字节字符串
    client_socket.send(struct.pack('I', len(bytes_str_ls_dict)))  # 将字节字符串的长度打包为4字节，发送到客户端
    client_socket.send(bytes_str_ls_dict)  # 将字节字符串发送到客户端


def server_gets_file(recv_cmd, client_socket):
    file_name = recv_cmd[5:]  # 获取要下载的文件名
    print(file_name)
    try:
        file = open(file_name, 'rb')  # 以二进制读模式打开文件
        file_content = file.read()  # 读取文件内容
        file.close()

        client_socket.send(b'0' + struct.pack('I', len(file_content)))  # 发送成功标志和文件内容的长度
        client_socket.send(file_content)  # 发送文件内容

    except FileNotFoundError:
        client_socket.send(b'1')  # 发送失败标志


def server_puts_file(recv_cmd, client_socket):
    file_name = recv_cmd[5:]  # 获取要上传的文件名
    print(file_name)
    file = open(file_name, 'wb')  # 以二进制写模式打开文件
    bytes_file_content_len = client_socket.recv(4)  # 接收文件内容长度的4字节
    file_content_len = struct.unpack('I', bytes_file_content_len)  # 解包得到文件内容的长度
    file_content = client_socket.recv(file_content_len[0])  # 接收文件内容
    file.write(file_content)  # 将文件内容写入文件
    file.close()


def server_remove_file(recv_cmd, client_socket):
    file_name = recv_cmd[7:]  # 获取要删除的文件名
    for i in os.listdir('.'):  # 遍历当前目录下的所有文件和目录
        if i == file_name and os.path.isfile(i):  # 如果找到了指定的文件并且它是一个普通文件
            client_socket.send(b'0')  # 发送成功标志
            os.remove(file_name)  # 删除指定文件
            client_socket.send(b'remove success')  # 发送删除成功的消息
            break  # 跳出循环
    else:
        client_socket.send(b'1')  # 发送失败标志


def server_cd(recv_cmd, client_socket):
    dir_name = recv_cmd[3:]  # 获取要切换的目录名
    for i in os.listdir('.'):  # 遍历当前目录下的所有文件和目录
        if i == dir_name and os.path.isdir(i):  # 如果找到了指定的目录并且它是一个目录
            client_socket.send(b'0')  # 发送成功标志
            os.chdir(dir_name)  # 切换到指定目录
            str1 = 'Now path is {}'.format(os.getcwd())  # 获取当前工作目录，并构造提示信息
            client_socket.send(str1.encode('utf-8'))  # 发送提示信息
            break  # 跳出循环
    else:
        client_socket.send(b'1')  # 发送失败标志


def server_pwd(client_socket):
    path = os.getcwd()  # 获取当前工作目录
    client_socket.send(path.encode('utf-8'))  # 发送当前工作目录


def child_handler(client_socket,client_addr):
    while True:
        encoding_recv_cmd = client_socket.recv(1024)  # 接收客户端发送的命令
       # if not encoding_recv_cmd:
       #     print(client_addr+'is close')
       #     client_socket.close()
       #     break
        recv_cmd = encoding_recv_cmd.decode('utf-8')  # 将接收到的字节串解码为字符串
        print(recv_cmd)  # 打印接收到的命令
        if recv_cmd == 'ls':
            server_ls(client_socket)  # 执行列出文件列表的操作
        elif recv_cmd[0:4] == 'gets':
            server_gets_file(recv_cmd, client_socket)  # 执行下载文件的操作
        elif recv_cmd[0:4] == 'puts':
            server_puts_file(recv_cmd, client_socket)  # 执行上传文件的操作
        elif recv_cmd[0:6] == 'remove':
            server_remove_file(recv_cmd, client_socket)  # 执行删除文件的操作
        elif recv_cmd[0:2] == 'cd':
            server_cd(recv_cmd, client_socket)  # 执行切换目录的操作
        elif recv_cmd[0:3] == 'pwd':
            server_pwd(client_socket)

    return 0


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    local_addr = ('192.168.88.129', 7788)
    server_socket.bind(local_addr)
    server_socket.listen(128)
    po = Pool(3) # 最大进程数设置为3
    while True:
        client_socket, client_addr = server_socket.accept()
        # 使用apply_async()方法将child_handler函数作为一个异步任务（async）提交到进程池中
        po.apply_async(child_handler, (client_socket,client_addr))
    po.close()
    po.join()
    server_socket.close()


if __name__ == '__main__':
    main()
