a = int(input("a:"))
b = int(input("b:"))
if a<=b:
    m = a
else:
    m = b
while(m>=1):
    if(a%m==0 and b%m==0):
        print("最大公约数："+str(m))
        break
    m -= 1