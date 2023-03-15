x = int(input("x:"))
a,b=1,1
print("1 1 ",end="")
while(a<=x and b<=x):
    c=a+b
    if(c>x):
        break
    else:
        a = b
        b = c
        print(c,end=" ")