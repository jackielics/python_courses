# 61. 读取某个字符串时间，将字符串的时间转换为时间戳（时间戳是以秒数来表示当前时间的一种时间形式）

import time
t = "2022-10-10 11:11:11"
timearray = time.strptime(t,r"%Y-%m-%d %H:%M:%S")
timerstamp = int(time.mktime(timearray))
print(timerstamp)