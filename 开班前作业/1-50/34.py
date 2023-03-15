# 写一个python list 的增删查改，list初始化几个元素自定


class py_list:
    def __init__(self):
        self.di={}
        # self.len = 0
        pass

    def initialize(self,len:int):
        for i in range(len):
            key = input("key:")
            self.di[key] = input("value:")

    def append(self):# 增
        key = input("key:")
        self.di[key] = input("value:")

    def delete(self):#删
        item = self.di.pop(input("key:"))
        print(item)

    def search(self):#查
        print(self.di[input("key:")])

    def change(self):#改
        key = input("key:")
        self.di[key] = input("value:")


pyli = py_list()
pyli.initialize(2)

while(True):
    cmd = int(input("1增2删3查4改5退出:"))
    if cmd == 5:
        break
    elif cmd==1:
        pyli.append()
    elif cmd==2:
        pyli.delete()
    elif cmd==3:
        pyli.search()
    elif cmd==4:
        pyli.change()
    print(pyli.di)