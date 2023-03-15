# Python 按键(key)或值(value)对字典进行排序（字典内容自定）
di = {0:0,1:1,2:2,3:3,-1:-1,-2:99}
kl = [i for i in di.keys()]
vl = [i for i in di.values()]

list_tuple = [i for i in di.items()]
list_sorted_by_key = sorted(list_tuple,key=lambda list_tuple:list_tuple[0])
list_sorted_by_val = sorted(list_tuple,key=lambda list_tuple:list_tuple[1])

print(list_sorted_by_key)
print(list_sorted_by_val)

