
# class MyProcess(multiprocessing.Process):     # 定义一个继承自Process类的MyProcess类
#     def run(self):                            # 重写run方法，在子进程中执行
#         f()

# p = MyProcess()          # 创建子进程p，类型为MyProcess
# p.start()                # 启动子进程p
# p.join()                 # 等待子进程p执行完毕

import multiprocessing
import os

def f():
    print('子进程ID:', os.getpid())

if __name__ == '__main__':
    print('主进程ID:', os.getpid())
    p = multiprocessing.Process(target=f)
    p.start()
    p.join()
    '''Windows 系统下，每个子进程都会自动导入主模块，并执行主模块中的代码，
    如果你的主模块中有一些与子进程相关的代码，可能会导致子进程无限递归地调用自己，
    最终导致程序崩溃。为了避免这个问题，通常建议在主模块中使用 
    if __name__ == '__main__': 来判断代码是否在主进程中执行，然后在 if 语句中调用子进程的代码。
    '''