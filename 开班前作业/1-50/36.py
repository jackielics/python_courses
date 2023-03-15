# 计算列表中10个元素的立方和（10个元素值自定）
li = [i for i in range(10)]
sum = 0
for i in range(len(li)):
    sum += i**3

print(sum)