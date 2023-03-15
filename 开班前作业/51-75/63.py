# 63. Python 将时间戳转换为字符串时间格式
import time
stamp = 1665371471
timestr = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(stamp))
print(timestr)