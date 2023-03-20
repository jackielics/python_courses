from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from django.template import loader
from .models import *
from django.db.models import Count


def my_render(request, template_path, context_dict={}):
    '''使用模板文件'''
    # 使用模板文件
    # 1.加载模板文件, 模板对象
    temp = loader.get_template(template_path)
    # 2.定义模板上下文:给模板文件传递数据，模板渲染:产生标准的html内容
    res_html = temp.render(context_dict)
    # 3.返回给浏览器
    return HttpResponse(res_html)


def index(request):
    # return HttpResponse('Hello Django')
    # return my_render(request,'index.html')
    # 例：查询所有图书的数目。
    # a=1+'a'
    print(BookInfo.objects.all().aggregate(Count('id')))
    return render(request, 'index.html', {'content': 'hello Django!!!'})


def index2(request):
    return HttpResponse('Hello Django3.2')


# 图书案例练习
def show_books(request):
    """
    显示图书的信息
    :param request:
    :return:
    """
    # 1.通过Models查找图书表中的数据
    books = BookInfo.objects.all()
    # 2 使用render进行模板数据替换
    return render(request, 'booktest/show_books.html', {'books': books})


# 图书的详情信息，展示图书下有多少英雄
def detail(request, bid):
    # 1.根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2.根据book查询关联的英雄信息
    heros = book.heroinfo_set.all()
    # 3 进行渲染
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})


# 删除对应的书籍
def delete(request, bid):
    # 1.根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2.删除对应书籍
    book.delete()
    # 3.重定向，让浏览器访问/show_books
    return HttpResponseRedirect('/show_books')


def create(request):
    '''新增一本图书'''
    # 1.创建BookInfo对象
    b = BookInfo()
    b.btitle = 'C语言开发宝典'
    b.bpub_date = date(2019, 10, 1)
    # 2.保存进数据库
    b.save()
    # 3.返回应答,让浏览器再访问/show_books,重定向
    return HttpResponseRedirect('/show_books')


def areas(request):
    '''获取广州市的上级地区和下级地区'''
    # 1.获取广州市的信息
    area = Areas.objects.get(atitle='广州市')
    # 2.查询广州市的上级地区
    parent = area.aParent
    # 3.查询广州市的下级地址
    children = area.areas_set.all()
    # 4 进行模板渲染
    return render(request, 'booktest/areas.html',
                  {'area': area, 'parent': parent, 'children': children})


# 展示登录页面
def login(request):
    # 判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已登录, 跳转到首页
        return redirect('/index')
    if 'username' in request.COOKIES:
        # 获取记住的用户名
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'booktest/login.html', {'username': username})


# request是一个HttpRequest对象
def login_check(request):
    # 练习QueryDict对象如何使用
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    print(username + ':' + password)

    # 获取用户输入验证码
    vcode1 = request.POST.get('vcode')
    # 获取session中保存的验证码
    vcode2 = request.session.get('verifycode')

    # 进行验证码校验
    if vcode1 != vcode2:
        # 验证码错误
        return redirect('/login')

    if username == 'admin' and password == '123':
        # 只有session中有islogin,就认为用户已登录
        request.session['islogin'] = True
        response = redirect('/index')
        if remember == 'on':  # 这个代表要记住用户名
            response.set_cookie('username', username, expires=datetime.now() + timedelta(days=14))
        return response
    else:
        return redirect('/login')
    # response=HttpResponse('ok')
    # return response


def test_ajax(request):
    '''显示ajax页面'''
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    '''ajax请求处理'''
    # 返回的json数据 {'res':1}
    return JsonResponse({'res': 1})


# 下面要实现异步登录效果
def login_ajax(request):
    '''显示异步登录页面'''
    return render(request, 'booktest/login_ajax.html')


# 异步请求时的用户名和密码验证
def login_ajax_check(request):
    # 1.获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2.进行校验,返回json数据
    if username == 'admin' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


# 设置cookie
from datetime import datetime, timedelta


# /set_cookie
def set_cookie(request):
    '''设置cookie信息'''
    response = HttpResponse('设置cookie') # 创建一个HttpResponse对象，用于响应，响应内容为“设置cookie”
    # cookie名为num, 值为2，过期时间为14天
    response.set_cookie('num', 2, max_age=14 * 24 * 3600)
    # 返回reponse
    return response


# 获取cookie
def get_cookie(request):
    '''获取cookie的信息'''
    num = request.COOKIES['num'] # 获取名字为num的cookie的值
    print(type(num))
    return HttpResponse(num) # 返回响应内容为num的值


# /set_session
def set_session(request):
    '''设置session，将session信息保存到服务器'''
    # session信息是字典类型
    request.session['username'] = 'admin'
    request.session['age'] = 18
    # request.session.set_expiry(5)
    return HttpResponse('设置session')


# /get_session
def get_session(request):
    '''获取session'''
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username + ':' + str(age))


# 　/clear_session
def clear_session(request):
    '''清除session信息'''
    # request.session.clear()  # 只是删除session_data
    request.session.flush() # 删除session_data和session_key
    return HttpResponse('清除成功')


# 验证不同变量在模板里替换都是使用点
def test_var(request):
    '''模板变量'''
    my_dict = {'title': '字典键值'}
    my_list = [1, 2, 3]
    book = BookInfo.objects.get(id=1) # 获取id为1的图书
    # 定义模板上下文
    context = {'my_dict': my_dict, 'my_list': my_list, 'book': book}
    # 使用模板，返回响应，响应内容为test_var.html
    return render(request, 'test_var.html', context) 


def test_tags(request):
    '''模板标签'''
    # 1. 查找所有图书的信息
    books = BookInfo.objects.all()
    return render(request, 'test_tags.html', {'books': books})


def test_filters(request):
    '''模板标签'''
    # 1. 查找所有图书的信息
    books = BookInfo.objects.all()
    return render(request, 'test_filters.html', {'books': books})


def test_base(request):
    return render(request, 'base.html')


def test_inherit(request):
    return render(request, 'child.html')


def html_escape(request):
    return render(request, 'html_escape.html', {'content': '<h1>hello</h1>'})


# 展示密码修改页面的
def change_pwd(request):
    return render(request, 'change_pwd.html')


def change_pwd_action(request):
    '''模拟修改密码处理'''
    # 1.获取新密码
    if request.session.has_key('islogin'): 
        # 判断用户是否登录
        pwd = request.POST.get('pwd') # 获取新密码，这里的pwd是change_pwd.html中的name属性
        # 2.返回一个应答
        return HttpResponse('修改密码为:%s'%pwd)
    else:
        return HttpResponse('未登录')


from PIL import Image, ImageDraw, ImageFont

# /verify_code
def verify_code(request):
    '''显示验证码图片'''
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高 RGB
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('STSONG.TTF', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')