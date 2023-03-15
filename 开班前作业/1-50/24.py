a = int(input("a:"))
b = int(input("b:"))
if a>=b:
    m = a
    n = b
else:
    m = b
    n = a
ts = 1
while(1):
    if(m*ts%n==0):
        print("最小公倍数："+str(m*ts))
        break
    ts += 1