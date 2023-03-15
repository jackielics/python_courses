# 62. 输入一个日期，输出3天前的日期的年月日
def getDaysNum(y:int,m:int)->int:
    if(y%4==0 and y%100!=0):
    # 年份是4的倍数，且不是100的倍数
        isrun = 1
    elif(y%100==0 and y%400==0):
        # 整百数，且必须是400的倍数
        isrun = 1
    else:
        isrun = 0
    if(m==2):
        return(28+isrun)
    elif(m<=7 and m%2==1):
        return(31)
    elif(m<=7 and m%2==0):
        return(30)
    elif(m>=8 and m%2==0):
        return(31)
    elif(m>=8 and m%2==1):
        return(30)


# 读取年，月，日，输出前三天日期
y = int(input("年："))
m = int(input("月："))
d = int(input("日："))
if(d<=3 and m==1):
    # xxxx.1.1/2/3
    y_y = y-1
    m_y = 12
    d_y = getDaysNum(y_y,m_y)-3+d
elif(d<=3):
    y_y = y
    m_y = m-1
    d_y = getDaysNum(y_y,m_y)-3+d
else:
    y_y = y
    m_y = m
    d_y = d-3
print(f"前三天是{y_y}/{m_y}/{d_y}")