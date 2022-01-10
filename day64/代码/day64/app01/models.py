from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    register_time = models.DateField()  # 年月日
    """
    DateField
    DateTimeField
        两个重要参数 
        auto_now:每次操作数据的时候 该字段会自动将当前时间更新
        auto_now_add:在创建数据的时候会自动将当前创建时间记录下来 之后只要不认为的修改 那么就一直不变
    """
    def __str__(self):
        return '对象:%s'%self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)

    # 一对多
    publish = models.ForeignKey(to='Publish')
    # 多对多
    authors = models.ManyToManyField(to='Author')


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()
    # varchar(254)  该字段类型不是给models看的 而是给后面我们会学到的校验性组件看的

    def __str__(self):
        return '对象:%s'%self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 一对一
    author_detail = models.OneToOneField(to='AuthorDetail')


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()  # 电话号码用BigIntegerField或者直接用CharField
    addr = models.CharField(max_length=64)