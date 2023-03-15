# 输入一个年和月，输出对应月天数
y = int(input("年："))
m = int(input("月："))
if(y%4==0 and y%100!=0):
    # 年份是4的倍数，且不是100的倍数
    isrun = 1
elif(y%100==0 and y%400==0):
    # 整百数，且必须是400的倍数
    isrun = 1
else:
    isrun = 0
if(m==2):
    print(28+isrun)
elif(m<=7 and m%2==1):
    print(31)
elif(m<=7 and m%2==0):
    print(30)
elif(m>=8 and m%2==0):
    print(31)
elif(m>=8 and m%2==1):
    print(30)