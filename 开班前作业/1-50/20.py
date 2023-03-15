import math
s = input("s:")
sum = 0
for i in range(len(s)):
    sum += math.pow(int(s[i]),3)
if(sum==int(s)):
    print("是")
else:
    print("不是")