from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.

def home(request):
    return render(request,'home.html')


def book_list(request):
    # 先查询出所有的书籍信息 传递给html页面
    book_queryset = models.Book.objects.all()
    return render(request,'book_list.html',locals())


def book_add(request):
    if request.method == 'POST':
        # 获取前端提交过来的所有数据
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish_date = request.POST.get("publish_date")
        publish_id = request.POST.get("publish")
        authors_list = request.POST.getlist("authors")  # [1,2,3,4,]
        # 操作数据库存储数据
        # 书籍表
        book_obj = models.Book.objects.create(title=title,price=price,publish_date=publish_date,publish_id=publish_id)
        # 书籍与作者的关系表
        book_obj.authors.add(*authors_list)
        # 跳转到书籍的展示页面
        """
        redirect括号内可以直接写url
        其实也可以直接写别名
        
        但是如果你的别名需要额外给参数的话，那么就必须使用reverse解析了
        """
        return redirect('book_list')


    # 先获取当前系统中所有的出版社信息和作者信息
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request,'book_add.html',locals())


def book_edit(request,edit_id):
    # 获取当前用户想要编辑的书籍对象 展示给用户看
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish_date = request.POST.get("publish_date")
        publish_id = request.POST.get("publish")
        authors_list = request.POST.getlist("authors")  # [1,2,3,4,]
        models.Book.objects.filter(pk=edit_id).update(title=title,
                                                      price=price,
                                                      publish_date=publish_date,
                                                      publish_id=publish_id
                                                      )
        # 该第三张关系表
        edit_obj.authors.set(authors_list)
        return redirect('book_list')

    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request,'book_edit.html',locals())


def book_delete(request,delete_id):
    # 简单粗暴 直接删除
    models.Book.objects.filter(pk=delete_id).delete()
    # 直接跳转到展示页
    return redirect('book_list')