# 70. Python 冒泡排序（列表元素自定）
src = [5,6,4,3,2,1,-2,-99,12,97835,98,100,-234,23,1,0]
# 
l = len(src)
for i in range(l-1,0,-1):
    # 从len-1到1，只剩一个时不用冒泡
    # print(i)
    for j in range(0,i):
        # print(j)
        if(src[j]>src[j+1]):
            # 交换元素
            temp = src[j]
            src[j] = src[j+1]
            src[j+1] = temp
print(src)