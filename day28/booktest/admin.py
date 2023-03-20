from django.contrib import admin

# Register your models here.
from booktest.models import BookInfo, HeroInfo,Areas,PicTest


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date','bread','bcomment']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcomment']


# 实现一次新增多条
class AreaStackedInline(admin.StackedInline):
    # 写多类的名字
    model = Areas
    extra = 2  #下面新增位置显示数目，默认显示3个


class AreasAdmin(admin.ModelAdmin):
    '''地区模型后台管理类'''
    list_per_page = 10  # 指定每页显示10条数据
    # 方法名也可以作为一列进行显示
    list_display = ['id', 'atitle', 'title', 'parent']
    actions_on_bottom = True  # 底部显示动作窗口
    actions_on_top = False  # 顶部不显示动作窗口
    list_filter = ['atitle']  # 列表页右侧过滤栏
    search_fields = ['atitle']  # 列表页上方的搜索框


    fields = ['aParent', 'atitle']
    # fieldsets = (
    #     ('基本', {'fields':['atitle']}),
    #     ('高级', {'fields':['aParent']})
    # )

    inlines = [AreaStackedInline]  #以块的形式
    # inlines = [AreaTabularInline]   #以表格的形式

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(Areas,AreasAdmin)
admin.site.register(PicTest)
