from django.test import TestCase

# Create your tests here.
import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day64.settings")
    import django
    django.setup()
    # 所有的代码都必须等待环境准备完毕之后才能书写
    from app01 import models

    # 增
    # res = models.User.objects.create(name='jason',age=18,register_time='2002-1-21')
    # print(res)
    # import datetime
    # ctime = datetime.datetime.now()
    # user_obj = models.User(name='egon',age=84,register_time=ctime)
    # user_obj.save()

    # 删
    # res = models.User.objects.filter(pk=2).delete()
    # print(res)
    """
    pk会自动查找到当前表的主键字段 指代的就是当前表的主键字段
    用了pk之后 你就不需要指代当前表的主键字段到底叫什么了
        uid
        pid
        sid
        ...
    """
    # user_obj = models.User.objects.filter(pk=1).first()
    # user_obj.delete()

    # 修改
    # models.User.objects.filter(pk=4).update(name='egonDSB')

    # user_obj = models.User.objects.get(pk=4)
    # user_obj = models.User.objects.filter(pk=6)
    """
    get方法返回的直接就是当前数据对象
    但是该方法不推荐使用
        一旦数据不存在该方法会直接报错
        而filter则不会
            所以我们还是用filter
    """
    # user_obj.name = 'egonPPP'
    # user_obj.save()


    # 必知必会13条
    # 1.all()  查询所有数据

    # 2.filter()     带有过滤条件的查询
    # 3.get()        直接拿数据对象 但是条件不存在直接报错
    # 4.first()      拿queryset里面第一个元素
    # res = models.User.objects.all().first()
    # print(res)
    # 5.last()
    # res = models.User.objects.all().last()
    # print(res)

    # 6.values()  可以指定获取的数据字段  select name,age from ...     列表套字典
    # res = models.User.objects.values('name','age')  # <QuerySet [{'name': 'jason', 'age': 18}, {'name': 'egonPPP', 'age': 84}]>
    # print(res)
    # 7.values_list()  列表套元祖
    # res = models.User.objects.values_list('name','age')  # <QuerySet [('jason', 18), ('egonPPP', 84)]>
    # print(res)
    # """
    #  # 查看内部封装的sql语句
    #  上述查看sql语句的方式  只能用于queryset对象
    #  只有queryset对象才能够点击query查看内部的sql语句
    #
    # """
    # 8.distinct()  去重
    # res = models.User.objects.values('name','age').distinct()
    # print(res)
    """
    去重一定要是一模一样的数据
    如果带有主键那么肯定不一样 你在往后的查询中一定不要忽略主键
    
    """
    # 9.order_by()
    # res = models.User.objects.order_by('age')  # 默认升序
    # res = models.User.objects.order_by('-age')  # 降序
    #
    # print(res)
    # 10.reverse()  反转的前提是 数据已经排过序了  order_by()
    # res = models.User.objects.all()
    # res1 = models.User.objects.order_by('age').reverse()
    # print(res,res1)

    # 11.count()  统计当前数据的个数
    # res = models.User.objects.count()
    # print(res)
    # 12.exclude()  排除在外
    # res = models.User.objects.exclude(name='jason')
    # print(res)

    # 13.exists()  基本用不到因为数据本身就自带布尔值  返回的是布尔值
    # res = models.User.objects.filter(pk=10).exists()
    # print(res)

    # 神奇的双下划线查询
    # 1 年龄大于35岁的数据
    # res = models.User.objects.filter(age__gt=35)
    # print(res)
    # 2 年龄小于35岁的数据
    # res = models.User.objects.filter(age__lt=35)
    # print(res)
    # 大于等于 小于等于
    # res = models.User.objects.filter(age__gte=32)
    # print(res)
    # res = models.User.objects.filter(age__lte=32)
    # print(res)

    # 年龄是18 或者 32 或者40
    # res = models.User.objects.filter(age__in=[18,32,40])
    # print(res)

    # 年龄在18到40岁之间的  首尾都要
    # res = models.User.objects.filter(age__range=[18,40])
    # print(res)

    # 查询出名字里面含有s的数据  模糊查询
    # res = models.User.objects.filter(name__contains='s')
    # print(res)
    #
    # 是否区分大小写  查询出名字里面含有p的数据  区分大小写
    # res = models.User.objects.filter(name__contains='p')
    # print(res)
    # 忽略大小写
    # res = models.User.objects.filter(name__icontains='p')
    # print(res)

    # res = models.User.objects.filter(name__startswith='j')
    # res1 = models.User.objects.filter(name__endswith='j')
    #
    # print(res,res1)


    # 查询出注册时间是 2020 1月
    # res = models.User.objects.filter(register_time__month='1')
    # res = models.User.objects.filter(register_time__year='2020')



    # 一对多外键增删改查
    # 增
    # 1  直接写实际字段 id
    # models.Book.objects.create(title='论语',price=899.23,publish_id=1)
    # models.Book.objects.create(title='聊斋',price=444.23,publish_id=2)
    # models.Book.objects.create(title='老子',price=333.66,publish_id=1)
    # 2  虚拟字段 对象
    # publish_obj = models.Publish.objects.filter(pk=2).first()
    # models.Book.objects.create(title='红楼梦',price=666.23,publish=publish_obj)

    # 删
    # models.Publish.objects.filter(pk=1).delete()  # 级联删除

    # 修改
    # models.Book.objects.filter(pk=1).update(publish_id=2)
    # publish_obj = models.Publish.objects.filter(pk=1).first()
    # models.Book.objects.filter(pk=1).update(publish=publish_obj)


    # 多对多  增删改查  就是在操作第三张表

    # 如何给书籍添加作者？
    # book_obj = models.Book.objects.filter(pk=1).first()
    # print(book_obj.authors)  # 就类似于你已经到了第三张关系表了
    # book_obj.authors.add(1)  # 书籍id为1的书籍绑定一个主键为1 的作者
    # book_obj.authors.add(2,3)

    # author_obj = models.Author.objects.filter(pk=1).first()
    # author_obj1 = models.Author.objects.filter(pk=2).first()
    # author_obj2 = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.add(author_obj)
    # book_obj.authors.add(author_obj1,author_obj2)
    """
    add给第三张关系表添加数据
        括号内既可以传数字也可以传对象 并且都支持多个
    """

    # 删
    # book_obj.authors.remove(2)
    # book_obj.authors.remove(1,3)

    # author_obj = models.Author.objects.filter(pk=2).first()
    # author_obj1 = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.remove(author_obj,author_obj1)
    """
    remove
        括号内既可以传数字也可以传对象 并且都支持多个
    """


    # 修改
    # book_obj.authors.set([1,2])  # 括号内必须给一个可迭代对象
    # book_obj.authors.set([3])  # 括号内必须给一个可迭代对象

    # author_obj = models.Author.objects.filter(pk=2).first()
    # author_obj1 = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.set([author_obj,author_obj1])  # 括号内必须给一个可迭代对象

    """
    set
        括号内必须传一个可迭代对象，该对象内既可以数字也可以对象 并且都支持多个
    """


    # 清空
    # 在第三张关系表中清空某个书籍与作者的绑定关系
    # book_obj.authors.clear()
    """
    clear
        括号内不要加任何参数
    
    """

    # 基于对象的跨表查询

    # 1.查询书籍主键为1的出版社
    # book_obj = models.Book.objects.filter(pk=1).first()
    # # 书查出版社 正向
    # res = book_obj.publish
    # print(res)
    # print(res.name)
    # print(res.addr)

    # 2.查询书籍主键为2的作者
    # book_obj = models.Book.objects.filter(pk=2).first()
    # # 书查作者 正向
    # # res = book_obj.authors  # app01.Author.None
    # res = book_obj.authors.all()  # <QuerySet [<Author: Author object>, <Author: Author object>]>
    #
    # print(res)

    # 3.查询作者jason的电话号码
    # author_obj = models.Author.objects.filter(name='jason').first()
    # res = author_obj.author_detail
    # print(res)
    # print(res.phone)
    # print(res.addr)

    """
    在书写orm语句的时候跟写sql语句一样的
    不要企图一次性将orm语句写完 如果比较复杂 就写一点看一点
    
    正向什么时候需要加.all()
        当你的结果可能有多个的时候就需要加.all()
        如果是一个则直接拿到数据对象
            book_obj.publish
            book_obj.authors.all()
            author_obj.author_detail
    """
    # 4.查询出版社是东方出版社出版的书
    # publish_obj = models.Publish.objects.filter(name='东方出版社').first()
    # 出版社查书  反向
    # res = publish_obj.book_set  # app01.Book.None
    # res = publish_obj.book_set.all()
    # print(res)

    # 5.查询作者是jason写过的书
    # author_obj = models.Author.objects.filter(name='jason').first()
    # 作者查书      反向
    # res = author_obj.book_set  # app01.Book.None
    # res = author_obj.book_set.all()
    # print(res)

    # 6.查询手机号是110的作者姓名
    # author_detail_obj = models.AuthorDetail.objects.filter(phone=110).first()
    # res = author_detail_obj.author
    # print(res.name)
    """
    基于对象 
        反向查询的时候
            当你的查询结果可以有多个的时候 就必须加_set.all()
            当你的结果只有一个的时候 不需要加_set.all()
        自己总结出 自己方便记忆的即可 每个人都可以不一样
    """


    # 基于双下划线的跨表查询


    # 1.查询jason的手机号和作者姓名
    # res = models.Author.objects.filter(name='jason').values('author_detail__phone','name')
    # print(res)
    # 反向
    # res = models.AuthorDetail.objects.filter(author__name='jason')  # 拿作者姓名是jason的作者详情
    # res = models.AuthorDetail.objects.filter(author__name='jason').values('phone','author__name')
    # print(res)


    # 2.查询书籍主键为1的出版社名称和书的名称
    # res = models.Book.objects.filter(pk=1).values('title','publish__name')
    # print(res)
    # 反向
    # res = models.Publish.objects.filter(book__id=1).values('name','book__title')
    # print(res)

    # 3.查询书籍主键为1的作者姓名
    # res = models.Book.objects.filter(pk=1).values('authors__name')
    # print(res)
    # 反向
    # res = models.Author.objects.filter(book__id=1).values('name')
    # print(res)


    # 查询书籍主键是1的作者的手机号
    # book author authordetail
    # res = models.Book.objects.filter(pk=1).values('authors__author_detail__phone')
    # print(res)
    """
    你只要掌握了正反向的概念
    以及双下划线
    那么你就可以无限制的跨表
    
    """


















