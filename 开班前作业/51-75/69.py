# 69. Python 选择排序（列表元素自定）
src = [5,6,4,3,2,1,-2,-99,12,97835,98,100,-234,23,1,0]

def findMin(src:list)->int:
    # 返回src中最小元素的下标
    m = min(src)

    for i,j in enumerate(src):
        if(j == m):
            return i

def swap(src,i,idx)->list:
    temp = src[i]
    src[i] = src[idx]
    src[idx] = temp
    return src

for i in range(len(src)-1):
    # 先找最小，只剩一个元素时不用管
    idx = findMin(src[i:]) + i
    # 然后交换元素位置
    src = swap(src,i,idx).copy()
    print(idx)

print(src)