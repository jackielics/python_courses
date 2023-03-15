# Python 数组翻转指定个数的元素（list内的元素自定）

li = [i for i in range(20)]
num = int(input("翻转个数："))
li2 = li[:num]
li2.reverse()
li[:num] = li2
# print(li[:num].reverse())
print(li)