# Python 移除字典A和字典B中共同存在的键值对，各自独有的不移除（字典内容自定）

da = {0:0,1:1,2:2,3:3,-1:-1,-2:99}
db = {0:0,1:1,2:2,3:3,4:4,5:5,-1:0}
for i in da.copy():
    if db.get(i) != None and db.get(i) == da.get(i):
        db.pop(i)
        da.pop(i)

print(db,da)