# 66. Python 线性查找（列表元素自定）
src = [i for i in range(100)]
tar = 100

for i in src:
    if(src[i] == tar):
        print(f"FOUND!  idx:{i}")
        break

if(i == len(src)-1):
    print("NOT FOUND!")