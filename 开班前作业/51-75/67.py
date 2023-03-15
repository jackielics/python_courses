# 67. Python 插入排序（列表元素自定）
# src = [9,23,1,0,-3,78,56,22,11,99,32]
src = [5,6,4,3,2,1,-2,-99,12,97835,98,100,-234,23,1,0]

def move(tar=3,OrdLi=[1,2,3],pos=1)->list:
    # 移动元素
    tar_list = [tar]
    OrdLi_fore = OrdLi[:pos]
    OrdLi_back = OrdLi[pos:-1]

    OrdLi_fore.extend(tar_list)
    OrdLi_fore.extend(OrdLi_back)
    return OrdLi_fore

def findPos(tar,OrdLi)->int:
    # 找出目标元素tar在目标数组list当中应有的位置
    if tar < OrdLi[0]:
        # 小于最小的
        return 0
    for i in range(len(OrdLi)-1,-1,-1):
        if(tar > OrdLi[i]):
            return i+1 # 大于前一个，则尾随其后
        pass

for i in range(1,len(src)): # 第一个元素不需要移动
    # tar是当前需要移动的目标
    print(src[i])
    pos = findPos(src[i],src[:i+1])
    src[:i+1] = move(src[i],src[:i+1],pos)

print(src)