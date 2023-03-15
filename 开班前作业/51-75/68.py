# 68. Python 快速排序（列表元素自定）
src = [5,6,4,3,2,1,-2,-99,12,97835,98,100,-234,23,1,0]
a=[3,4,2,1,5]

def QuickSort(src = [5,6,4,3,2,1,-2,-99,12,97835,98,100,-234,23,1,0],left=0,right=len(src)-1)->list:
    # 一次划分，小左大右
    pivot = left # 以最左端为pivot
    while(left<right):
        while(src[left]<=src[pivot]):# 在左边找大于pivot的
            left += 1
        while(src[right]>=src[pivot]):# 在右边找小于pivot的
            right -= 1
        # 交换
        temp = src[left]
        src[left] = src[right]
        src[right] = temp
