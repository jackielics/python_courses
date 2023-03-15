#! /usr/bin/python3
# author claude

from socket import *
import struct
import os


def client_ls():
    client_socket.send(b'ls')

    bytes_ls_dict_len = client_socket.recv(4)
    ls_dict_len = struct.unpack('I', bytes_ls_dict_len)

    bytes_str_ls_dict = client_socket.recv(ls_dict_len[0])
    str_ls_dict = bytes_str_ls_dict.decode('utf-8')
    ls_dict = eval(str_ls_dict)

    for key in ls_dict:
        print('{:>4}{:>10}{:>20}'.format(ls_dict[key][0], ls_dict[key][1], key))


def client_gets_file(cmd):
    client_socket.send(cmd.encode('utf-8'))
    no_file_flag = client_socket.recv(1)
    if no_file_flag == b'1':
        print('No such file in server')
    else:
        bytes_file_content_len = client_socket.recv(4)
        file_content_len = struct.unpack('I', bytes_file_content_len)
        file_content = client_socket.recv(file_content_len[0])

        file = open(cmd[5:], 'wb')
        file.write(file_content)
        file.close()


def client_puts_file(cmd):
    file_name = cmd[5:]
    try:
        file = open(file_name, 'rb')
        file_content = file.read()
        file.close()

        client_socket.send(cmd.encode('utf-8'))
        client_socket.send(struct.pack('I', len(file_content)))
        client_socket.send(file_content)
    except FileNotFoundError:
        print('No such file')


def client_remove_file(cmd):
    client_socket.send(cmd.encode('utf-8'))
    no_such_file_flag = client_socket.recv(1)
    if no_such_file_flag == b'1':
        print('No such file in server')
    else:
        recv_data = client_socket.recv(1024)
        print(recv_data.decode('utf-8'))


def client_cd(cmd):
    client_socket.send(cmd.encode('utf-8'))
    no_such_dir_flag = client_socket.recv(1)
    if no_such_dir_flag == b'1':
        print('No such dir in server')
    else:
        recv_data = client_socket.recv(1024)
        print(recv_data.decode('utf-8'))


def client_pwd():
    client_socket.send(cmd.encode('utf-8'))
    bytes_path = client_socket.recv(1024)
    print(bytes_path.decode('utf-8'))


client_socket = socket(AF_INET, SOCK_STREAM)
server_addr = ('192.168.157.130', 7788)
client_socket.connect(server_addr)
client_name = input('请输入用户名:')

while True:
    cmd = input(client_name + ':')
    if cmd == 'ls':
        client_ls()
    elif cmd[0:4] == 'gets':
        client_gets_file(cmd)
    elif cmd[0:4] == 'puts':
        client_puts_file(cmd)
    elif cmd[0:6] == 'remove':
        client_remove_file(cmd)
    elif cmd[0:2] == 'cd':
        client_cd(cmd)
    elif cmd[0:3] == 'pwd':
        client_pwd()

client_socket.close()
