asc = " !\"#$%&`()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[/]^_`abcdefghijklmnopqrstuvwxyz{|}~"
x = input("字符:")
print(32+asc.find(x))
y = int(input("ASCII:"))
print(asc[y-32])