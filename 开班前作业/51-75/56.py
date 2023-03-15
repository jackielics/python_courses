# Python 对字符串切片及翻转（字符串内容自定）
s = "a = 10000"
ss = s[1:5]
sl = list(ss)
sl.reverse()
s2 = ''.join(sl)
print(s2)