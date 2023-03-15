# -*- coding:utf-8 -*-
# 修改import 中的Queue 为Manager
from multiprocessing import Manager,Pool
import os,time,random
def reader(q):
    print("reader 启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader 从Queue 获取到消息：%s" % q.get(True))
def writer(q):
    print("writer 启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "wangdao":
        q.put(i)
    time.sleep(2)

if __name__=="__main__":
    print("(%s) start" % os.getpid())
    q = Manager().Queue() # 使用Manager 中的Queue
    po = Pool()
    po.apply_async(writer, (q,))
    time.sleep(1) # 先让上面的任务向Queue 存入数据，然后再让下面的任务开始从中取数据
    po.apply_async(reader, (q,))
    po.close()
    po.join()
    print("(%s) End" % os.getpid())