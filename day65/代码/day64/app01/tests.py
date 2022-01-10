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

    # 聚合查询      aggregate
    """
    聚合查询通常情况下都是配合分组一起使用的
    只要是跟数据库相关的模块 
        基本上都在django.db.models里面
        如果上述没有那么应该在django.db里面
    """
    # from app01 import models
    # from django.db.models import Max,Min,Sum,Count,Avg
    # # 1 所有书的平均价格
    # # res = models.Book.objects.aggregate(Avg('price'))
    # # print(res)
    # # 2.上述方法一次性使用
    # res = models.Book.objects.aggregate(Max('price'),Min('price'),Sum('price'),Count('pk'),Avg('price'))
    # print(res)


    # 分组查询  annotate
    """
    MySQL分组查询都有哪些特点
        分组之后默认只能获取到分组的依据 组内其他字段都无法直接获取了
            严格模式
                ONLY_FULL_GROUP_BY
                
    """
    from django.db.models import Max, Min, Sum, Count, Avg
    # 1.统计每一本书的作者个数
    # res = models.Book.objects.annotate()  # models后面点什么 就是按什么分组
    # res = models.Book.objects.annotate(author_num=Count('authors')).values('title','author_num')
    """
    author_num是我们自己定义的字段 用来存储统计出来的每本书对应的作者个数
    """
    # res1 = models.Book.objects.annotate(author_num=Count('authors__id')).values('title','author_num')
    # print(res,res1)
    """
    代码没有补全 不要怕 正常写
    补全给你是pycharm给你的 到后面在服务器上直接书写代码 什么补全都没有 颜色提示也没有
    
    """

    # 2.统计每个出版社卖的最便宜的书的价格(作业:复习原生SQL语句 写出来)
    # res = models.Publish.objects.annotate(min_price=Min('book__price')).values('name','min_price')
    # print(res)

    # 3.统计不止一个作者的图书
        # 1.先按照图书分组 求每一本书对应的作者个数
        # 2.过滤出不止一个作者的图书
    # res = models.Book.objects.annotate(author_num=Count('authors')).filter(author_num__gt=1).values('title','author_num')
    # """
    # 只要你的orm语句得出的结果还是一个queryset对象
    # 那么它就可以继续无限制的点queryset对象封装的方法
    #
    # """
    # print(res)

    # 4.查询每个作者出的书的总价格
    # res = models.Author.objects.annotate(sum_price=Sum('book__price')).values('name','sum_price')
    # print(res)


    """
    如果我想按照指定的字段分组该如何处理呢？
        models.Book.objects.values('price').annotate()
    后续BBS作业会使用
    
    
    你们的机器上如果出现分组查询报错的情况
        你需要修改数据库严格模式
    """


    # F与Q查询
    # 1.查询卖出数大于库存数的书籍
    # F查询
    """
    能够帮助你直接获取到表中某个字段对应的数据
    """
    from django.db.models import F
    # res = models.Book.objects.filter(maichu__gt=F('kucun'))
    # print(res)


    # 2.将所有书籍的价格提升500块
    # models.Book.objects.update(price=F('price') + 500)


    # 3.将所有书的名称后面加上爆款两个字
    """
    在操作字符类型的数据的时候 F不能够直接做到字符串的拼接
    """
    # from django.db.models.functions import Concat
    # from django.db.models import Value
    # models.Book.objects.update(title=Concat(F('title'), Value('爆款')))
    # models.Book.objects.update(title=F('title') + '爆款')  # 所有的名称会全部变成空白

    # Q查询
    # 1.查询卖出数大于100或者价格小于600的书籍
    # res = models.Book.objects.filter(maichu__gt=100,price__lt=600)
    """filter括号内多个参数是and关系"""
    # from django.db.models import Q
    # res = models.Book.objects.filter(Q(maichu__gt=100),Q(price__lt=600))  # Q包裹逗号分割 还是and关系
    # res = models.Book.objects.filter(Q(maichu__gt=100)|Q(price__lt=600))  # | or关系
    # res = models.Book.objects.filter(~Q(maichu__gt=100)|Q(price__lt=600))  # ~ not关系
    # print(res)  # <QuerySet []>

    # Q的高阶用法  能够将查询条件的左边也变成字符串的形式
    # q = Q()
    # q.connector = 'or'
    # q.children.append(('maichu__gt',100))
    # q.children.append(('price__lt',600))
    # res = models.Book.objects.filter(q)  # 默认还是and关系
    # print(res)


    # 事务
    # from django.db import transaction
    # try:
    #     with transaction.atomic():
    #         # sql1
    #         # sql2
    #         ...
    #         # 在with代码快内书写的所有orm操作都是属于同一个事务
    # except Exception as e:
    #     print(e)
    # print('执行其他操作')

    # res = models.Book.objects.all()
    # print(res)  # 要用数据了才会走数据库

    # 想要获取书籍表中所有数的名字
    # res = models.Book.objects.values('title')
    # for d in res:
    #     print(d.get('title'))
    # 你给我实现获取到的是一个数据对象 然后点title就能够拿到书名 并且没有其他字段
    # res = models.Book.objects.only('title')
    # res = models.Book.objects.all()
    # print(res)  # <QuerySet [<Book: 三国演义爆款>, <Book: 红楼梦爆款>, <Book: 论语爆款>, <Book: 聊斋爆款>, <Book: 老子爆款>]>
    # for i in res:
        # print(i.title)  # 点击only括号内的字段 不会走数据库
        # print(i.price)  # 点击only括号内没有的字段 会重新走数据库查询而all不需要走了

    res = models.Book.objects.defer('title')  # 对象除了没有title属性之外其他的都有
    for i in res:
        print(i.price)
    """
    defer与only刚好相反
        defer括号内放的字段不在查询出来的对象里面 查询该字段需要重新走数据
        而如果查询的是非括号内的字段 则不需要走数据库了

    """

    # select_related与prefetch_related  跟跨表操作有关
    # res = models.Book.objects.all()
    # for i in res:
    #     print(i.publish.name)  # 每循环一次就要走一次数据库查询

    # res = models.Book.objects.select_related('authors')  # INNER JOIN
    """
    select_related内部直接先将book与publish连起来 然后一次性将大表里面的所有数据
    全部封装给查询出来的对象
        这个时候对象无论是点击book表的数据还是publish的数据都无需再走数据库查询了
    
    select_related括号内只能放外键字段    一对多 一对一
        多对多也不行
    
    """
    # for i in res:
    #     print(i.publish.name)  # 每循环一次就要走一次数据库查询

    res = models.Book.objects.prefetch_related('publish')  # 子查询
    """
    prefetch_related该方法内部其实就是子查询
        将子查询查询出来的所有结果也给你封装到对象中
        给你的感觉好像也是一次性搞定的
    """
    for i in res:
        print(i.publish.name)

















