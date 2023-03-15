s = input("表达式：")
if(s.find("+")>-1):
    a = float(s[:s.find("+")])
    b = float(s[s.find("+")+1:])
    print(a+b)
elif(s.find("-")>-1):
    a = float(s[:s.find("-")])
    b = float(s[s.find("-")+1:])
    print(a-b)
elif(s.find("*")>-1):
    a = float(s[:s.find("*")])
    b = float(s[s.find("*")+1:])
    print(a*b)
elif(s.find("/")>-1):
    a = float(s[:s.find("/")])
    b = float(s[s.find("/")+1:])
    print(a/b)