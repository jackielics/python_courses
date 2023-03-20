# 作者: 王道 龙哥
# 2023年03月18日11时31分37秒
# 过滤器其实就是python函数
from django.template import Library

# 创建一个Library类的对象
register = Library()

# 自定义的过滤器函数，至少有一个参数，最多两个
@register.filter
def mod(num):
    return num%2


@register.filter
def mod_val(num, val):
    '''判断num是否能被val整除'''
    return num%val == 0