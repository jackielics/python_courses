from django.db import models


# 继承模型管理器类，重写all方法，实现软删除
class BookInfoManager(models.Manager):
    def all(self):
        # 1.调用父类的all方法，获取所有数据
        books = super().all()
        # 2.对books中的数据进行过滤
        books_nodel = books.filter(isDelete=False)
        # 返回books
        return books_nodel
    # 2.封装方法，操作模型类对应的数据表（增删改查)
    def create_book(self, btitle, bpub_date):
        '''添加一本图书'''
        # 1.创建一个图书对象
        # 获取self所在的模型类
        model_class = self.model
        book = model_class()
        # 也可以像下面这样写，但是不推荐，因为如果模型类名字改了，这里就要改
        # book = BookInfo() 
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 2.添加进数据库
        book.save()
        # 3.返回book
        return book

# Create your models here.
class BookInfo(models.Model): 
    """ 模型类，继承models.Model作用：
        1.告诉Django这是一个模型类 
        2.创建一个模型类对应的数据库表 """
    btitle = models.CharField(max_length=20, db_index=True)
    # 价格,最大位数为10,小数为2
    bprice = models.DecimalField(default=10, max_digits=10, decimal_places=2)
    bpub_date = models.DateField(auto_now=True)
    # 阅读量，blank是控制后台管理的
    bread = models.IntegerField(default=0, null=True, blank=True)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)
    #属性重写
    objects = BookInfoManager()

    def __str__(self):
        '''定义每个数据对象的显示信息，显示在管理页面'''
        return self.btitle

    class Meta:
        """ 指定模型类对应的数据表名 """
        db_table = 'bookinfo'

# 英雄模型类，关联BookInfo模型类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=100)  # 拥有什么技能
    # 关联图书，级联删除，不创建外键约束
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE, db_constraint=False)
    # 删除标记
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname


# 选课的多对多的实现
# 一个老师要教多个学生时，当前对象.关联对象_set.add
class Teacher(models.Model):
    tname = models.CharField(max_length=20)

    def __str__(self):
        return self.tname


# 一个学生可以选多个老师，那么新增时，就直接使用多对多字段，select_course
class Student(models.Model):
    sname = models.CharField(max_length=20)
    select_course = models.ManyToManyField('Teacher')

    def __str__(self):
        return self.sname


# 员工基本信息类
class EmployeeBasicInfo(models.Model):
    # 姓名
    name = models.CharField(max_length=20)
    # 性别
    gender = models.BooleanField(default=False)
    # 年龄
    age = models.IntegerField()
    # 关系属性,代表员工的详细信息
    # employee_detail = models.OneToOneField('EmployeeDetailInfo',on_delete=models.CASCADE,)


# 员工详细信息类
class EmployeeDetailInfo(models.Model):
    # 联系地址
    addr = models.CharField(max_length=256)
    # 教育经历
    # 关系属性，代表员工基本信息
    employee_basic = models.OneToOneField('EmployeeBasicInfo', on_delete=models.CASCADE, )


class Areas(models.Model):
    '''地区模型类'''
    # 地区名称
    atitle = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, )

    def __str__(self):
        return self.atitle

    def title(self):
        '''返回当前地区的名称'''
        return self.atitle

    def parent(self):
        '''返回当前地区的父级地区名称'''
        if self.aParent is None:
            return ''
        return self.aParent.atitle
    parent.short_description = '父级地区名称' # 设置admin中显示的列名

class PicTest(models.Model):
    '''上传图片'''
    goods_pic = models.ImageField(upload_to='booktest') # upload_to指定图片上传的途径