s = input("")
# Python读取字符串，如果字符串是纯小写，就变为大写输出，如果存在一个大写，就全部转为小写输出

if s.islower():
    # 全是小写
    print(s.upper())
else:
    print(s.lower())
