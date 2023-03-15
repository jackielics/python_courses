# Python 判断字符串是否存在子字符串 （字符串内容自定）
s1 = "asdfghjk"
s2 = "fghj"
# print(s1.find(s2))
if s1.find(s2)==-1:
    print("存在")
else:
    print("不存在")