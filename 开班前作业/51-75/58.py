# Python 计算字典值之和（字典内容自定）

di = {0:0,1:1,2:2,3:3,-1:-1,-2:99}
sum = 0
for i in di:
    sum += di[i]

print(sum)