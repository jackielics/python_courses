import multiprocessing
import os
class MyProcess(multiprocessing.Process):     # 定义一个继承自Process类的MyProcess类
    def run(self):                            # 重写run方法，在子进程中执行
        f()

def f():
    print('子进程ID:', os.getpid())

if __name__ == '__main__':
    p = MyProcess()          # 创建子进程p，类型为MyProcess
    p.start()                # 启动子进程p
    p.join()                 # 等待子进程p执行完毕
