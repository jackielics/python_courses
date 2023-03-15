# Python 计算列表元素之积（list内的元素自定）
li = [i for i in range(10)]
prod = 1
for i in li:
    prod *= i

print(prod)