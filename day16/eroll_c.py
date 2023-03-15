import selectimport sys
tcp_server_socket=so
cket(AF INET,SOCK STREAM)
#重用对应地址和端口
tcp server socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#本地IP地址和端口
address = (’192.168.1.111'，2000)
tcp_server_socket. bind(address)#端口激活
tcp_server_socket.listen(10o)
client_socket,clientAddr = tcp_server_socket.accept()
print (clientAddr)|
# print(tcp_server_socket.fileno())# print (client_socket.fileno())
##创建一个epoll对象
epoll = select.epol1()
epoll.register(client_socket.fileno()， select.EPOLLIN)epoll.register(sys.stdin.fileno(), select.EPOLLIN)
