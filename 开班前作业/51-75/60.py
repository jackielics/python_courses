# Python 合并字典A和字典B（字典内容自定）

da = {-1:-1,-2:99}
db = {0:0,1:1,2:2,3:3,4:4,5:5}

for i in da:
    db[i] = da[i]

print(db)