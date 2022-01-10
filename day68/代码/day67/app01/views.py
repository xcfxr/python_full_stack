from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.


def index(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
    return render(request,'index.html')

import json
def ab_json(request):
    if request.is_ajax():
        # print(request.is_ajax())
        # print(request.POST)
        # print(request.FILES)
        # print(request.body)  # b'{"username":"jason","age":25}'
        # 针对json格式数据需要你自己手动处理
        json_bytes = request.body
        # json_str = json_bytes.decode('utf-8')
        # json_dict = json.loads(json_str)

        # json.loads括号内如果传入了一个二进制格式的数据那么内部自动解码再反序列化
        json_dict = json.loads(json_bytes)  # {'username': 'jason', 'age': 25} <class 'dict'>
        print(json_dict,type(json_dict))  # {'username': 'jason', 'age': 25} <class 'dict'>
    return render(request,'ab_json.html')


def ab_file(request):
    if request.is_ajax():
        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
    return render(request,'ab_file.html')

import json
from django.http import JsonResponse
from django.core import serializers
def ab_ser(request):
    user_queryset = models.User.objects.all()
    # [{},{},{},{},{}]
    # user_list = []
    # for user_obj in user_queryset:
    #     tmp = {
    #         'pk':user_obj.pk,
    #         'username':user_obj.username,
    #         'age':user_obj.age,
    #         'gender':user_obj.get_gender_display()
    #     }
    #     user_list.append(tmp)
    # return JsonResponse(user_list,safe=False)
    # return render(request,'ab_ser.html',locals())

    # 序列化
    res = serializers.serialize('json',user_queryset)
    """会自动帮你将数据变成json格式的字符串 并且内部非常的全面"""
    return HttpResponse(res)
"""
[
 {"pk": 1, "username": "jason", "age": 25, "gender": "male"}, 
 {"pk": 2, "username": "egon", "age": 31, "gender": "female"},
 {"pk": 3, "username": "kevin", "age": 32, "gender": "others"}, 
 {"pk": 4, "username": "tank", "age": 40, "gender": 4}
 ]
前后端分离的项目
    作为后端开发的你只需要写代码将数据处理好
    能够序列化返回给前端即可 
        再写一个接口文档 告诉前端每个字段代表的意思即可
        
        
[
{   "model": "app01.user", 
    "pk": 1, 
    "fields": {"username": "jason", "age": 25, "gender": 1}}, 
    
{   "model": "app01.user", 
    "pk": 2, 
    "fields": {"username": "egon", "age": 31, "gender": 2}}, 
    
{   "model": "app01.user", 
    "pk": 3, 
    "fields": {"username": "kevin", "age": 32, "gender": 3}},
     
{   "model": "app01.user", 
    "pk": 4, 
    "fields": {"username": "tank", "age": 40, "gender": 4}}
]
写接口就是利用序列化组件渲染数据然后写一个接口文档 该交代交代一下就完事
"""

def user_list(request):
    user_queryset = models.User.objects.all()
    return render(request,'user_list.html',locals())

import time
def delete_user(request):
    """
    前后端在用ajax进行交互的时候 后端通常给ajax的回调函数返回一个字典格式的数据
    :param request:
    :return:
    """
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {"code":1000,'msg':''}
            time.sleep(3)  # 模拟操作数据的延迟
            delete_id = request.POST.get('delete_id')
            models.User.objects.filter(pk=delete_id).delete()
            back_dic['msg'] = '数据已经删了，你赶紧跑路!'
            # 我们需要告诉前端我们操作的结果
            return JsonResponse(back_dic)

from utils.mypage import Pagination

def ab_pl(request):
    # 先给Book插入一万条数据
    # for i in range(10000):
    #     models.Book.objects.create(title='第%s本书'%i)
    # # 再将所有的数据查询并展示到前端页面
    # book_queryset = models.Book.objects.all()

    # 批量插入
    # book_list = []
    # for i in range(100000):
    #     book_obj = models.Book(title='第%s本书'%i)
    #     book_list.append(book_obj)
    # models.Book.objects.bulk_create(book_list)
    """
    当你想要批量插入数据的时候 使用orm给你提供的bulk_create能够大大的减少操作时间
    :param request: 
    :return: 
    """
    # # 分页
    # book_list = models.Book.objects.all()
    #
    # # 想访问哪一页
    # current_page = request.GET.get('page',1)  # 如果获取不到当前页码 就展示第一页
    # # 数据类型转换
    # try:
    #     current_page = int(current_page)
    # except Exception:
    #     current_page = 1
    # # 每页展示多少条
    # per_page_num = 10
    # # 起始位置
    # start_page = (current_page - 1) * per_page_num
    # # 终止位置
    # end_page = current_page * per_page_num
    #
    # # 计算出到底需要多少页
    # all_count = book_list.count()
    #
    # page_count, more = divmod(all_count, per_page_num)
    # if more:
    #     page_count += 1
    #
    # page_html = ''
    # xxx = current_page
    # if current_page < 6:
    #     current_page = 6
    # for i in range(current_page-5,current_page+6):
    #     if xxx == i:
    #         page_html += '<li class="active"><a href="?page=%s">%s</a></li>'%(i,i)
    #     else:
    #         page_html += '<li><a href="?page=%s">%s</a></li>'%(i,i)
    #
    #
    #
    # book_queryset =  book_list[start_page:end_page]
    book_queryset = models.Book.objects.all()
    current_page = request.GET.get('page',1)
    all_count = book_queryset.count()

    # 1 传值生成对象
    page_obj = Pagination(current_page=current_page,all_count=all_count)
    # 2 直接对总数据进行切片操作
    page_queryset = book_queryset[page_obj.start:page_obj.end]
    # 3 将page_queryset传递到页面 替换之前的book_queryset
    return render(request,'ab_pl.html',locals())
"""
per_page_num = 10
current_page                start_page                  end_page
    1                           0                           10
    2                           10                          20
    3                           20                          30
    4                           30                          40


per_page_num = 5
current_page                start_page                  end_page
    1                           0                           5
    2                           5                           10
    3                           10                          15
    4                           15                          20
    
start_page = (current_page - 1) * per_page_num
end_page = current_page * per_page_num
"""