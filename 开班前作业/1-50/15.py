a = int(input("a:"))
for i in range(2,a):
    if a%i==0:
        print("非质数")
        exit()
print("质数")