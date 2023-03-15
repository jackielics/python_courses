# Python 移除字符串中的指定位置字符（字符串内容自定，指定位置通过读取输入获取）
li = [i for i in range(10)]
no = int(input("位置："))
del li[no]
print(li)