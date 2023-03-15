# 65. Python 实现二分查找（列表元素自定）
sour = [i for i in range(100)]
tar = 31.2

low = 0
high = len(sour)-1
while(low<=high):
    mid = int((low+high)/2)
    if(sour[mid]==tar):
        print(f"FOUND!idx:{mid}")
        break
    elif(sour[mid]<tar):
        low = mid+1
    elif(sour[mid]>tar):
        high = mid-1
        
if(low>high):
    print("NOT FOUND!")