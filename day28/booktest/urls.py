# 作者: 王道 龙哥
# 2023年03月15日11时14分11秒
from django.urls import path
from .views import *
urlpatterns = [
    path('index/',index),
    path('index2/', index2),
    path('show_books/',show_books),
    path('books/<int:bid>',detail),
    path('delete<int:bid>',delete),
    path('create/',create),
    path('areas/',areas),
    path('login/',login),
    path('login_check/',login_check),
    path('test_ajax/',test_ajax),
    path('ajax_handle/',ajax_handle),
    path('login_ajax/',login_ajax),
    path('login_ajax_check/',login_ajax_check),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('clear_session/',clear_session),
    path('test_var/',test_var),
    path('test_tags/',test_tags),
    path('test_filters/',test_filters),
    path('test_base/',test_base),
    path('test_inherit/',test_inherit),
    path('html_escape/',html_escape),
    path('change_pwd/',change_pwd),
    path('change_pwd_action/',change_pwd_action),
    path('verify_code/',verify_code)
]