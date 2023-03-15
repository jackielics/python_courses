# Python 计算某个元素在列表中出现的次数（list内的元素个数自定）
li = [i for i in range(20)]
tar = int(input("target:"))
num = li.count(tar)
print(num)