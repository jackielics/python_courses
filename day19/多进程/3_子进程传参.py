# -*- coding:utf-8 -*-
from multiprocessing import Process
import os
from time import sleep
def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s,age=%d ,pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)

if __name__=='__main__':
    p = Process(target=run_proc, args=('test',18), kwargs={"m":20})
    p.start()
    sleep(1) # 1 秒中之后，立即结束子进程
    p.terminate() # 结束子进程
    p.join() # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print(p.exitcode) # 子进程的退出码，0 表示正常退出，-9 表示被强制终止