# Python 将列表中的指定位置（两个指定的位置通过读取输入来获取）的两个元素对调
li = [i for i in range(20)]
n1 = int(input("idx_1:"))
n2 = int(input("idx_2:"))
temp = li[n1]
li[n1] = li[n2]
li[n2] = temp
print(li)