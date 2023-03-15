# Python 将列表中的头尾两个元素对调（list内的元素自定）
li = [i for i in range(20)]
temp = li[-1]
li[-1] = li[0]
li[0] = temp
print(li)