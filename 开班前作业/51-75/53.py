# Python 使用正则表达式提取字符串中的 URL（字符串内容自定）
import re
s = "百度的网址是https://www.baidu.com"
pattern = "https://(www\..*\.com)"

res = re.search(pattern, s, flags=0)
print(res.group(1))