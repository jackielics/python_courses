def jzzh(x,jz):
    q = x #商
    r = 0 #余
    out = ""
    while(q>0):
        r = q%jz
        q = int(q/jz)
        out = str(r)+out
    return out

x = int(input("x十进制:"))
print("二进制："+jzzh(x,2))
print("八进制："+jzzh(x,8))
print("十六进制："+jzzh(x,16))