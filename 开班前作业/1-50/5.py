import math
x1 = int(input("x1:"))
x2 = int(input("x2:"))
x3 = int(input("x3:"))
if(x1+x2<=x3 or x1+x3<=x2 or x2+x3<=x1):
    print("illegal!")
else:
    p=x1+x2+x3
    s=math.sqrt(p*(p-x1)*(p-x2)*(p-x3))
    print("square："+str(s))