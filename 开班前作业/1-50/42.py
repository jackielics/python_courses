# Python 判断元素是否在列表中存在（list内的元素自定）
li = [i for i in range(20)]
target = int(input("target:"))
if target in li:
    print("元素存在")
else:
    print("元素不存在")