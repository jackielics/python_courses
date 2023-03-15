#代码4-3 c socket03c.py
#!/usr/bin/env python3
# coding:utf-8
import socket, time, sys, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)
s.connect(('192.168.157.130',8088))
filename='/bin/ls'
print('I want to get the file %s!' % filename)
s.send(filename.encode('utf-8'))
str1 = s.recv(1024) # 先recv yes或者no
str2 = str1.decode('utf-8')
if str2=='no':
    print('To get the file %s is failed!' % filename)
else:
    print(str2)
    s.send(b'I am ready!')
    temp = filename.split('/')
    myname = 'my_' + temp[len(temp)-1]
    size = 1024
    with open(myname, 'wb') as f:
        # 以二进制打开
        while True:
            data = s.recv(size)
            f.write(data)
            # f.flush()
            file_descriptor = f.fileno()
            file_stat = os.fstat(file_descriptor)
            print("len(data)", len(data))
            print("file_stat.st_size", file_stat.st_size)
            time.sleep(0.1)
            if len(data) < size:
                break
    print('The downloaded file is %s. Size: %d MB' % (myname, file_stat.st_size / 1024 / 1024))
s.close()