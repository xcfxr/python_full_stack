from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
# Create your views here.


"""
使用auth模块要用就用全套
"""

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去用户表中校验数据
        # 1.表如何获取
        # 2.密码如何比对
        user_obj = auth.authenticate(request,username=username,password=password)
        # print(user_obj)  # 用户对象  jason   数据不符合则返回None
        # print(user_obj.username)  # jason
        # print(user_obj.password)  # pbkdf2_sha256$36000$zeNDf8CkZj7y$b+e/CjzZoAnbBIpvUWgz25ybBDqDzRTmYAHPytxqRYQ=
        # 判断当前用户是否存在
        if user_obj:
            # 保存用户状态
            auth.login(request,user_obj)  # 类似于request.session[key] = user_obj
            # 主要执行了该方法 你就可以在任何地方通过request.user获取到当前登陆的用户对象
            return redirect('/home/')
        """
        1.自动查找auth_user标签
        2.自动给密码加密再比对
        该方法注意事项
            括号内必须同时传入用户名和密码
            不能只传用户名(一步就帮你筛选出用户对象)
        """
    return render(request,'login.html')


from django.contrib.auth.decorators import login_required


# @login_required(login_url='/login/')  # 局部配置:用户没有登陆跳转到login_user后面指定的网址
# @login_required  # 全局配置
# @login_required(login_url='/xxx/')  # 优先级  局部 > 全局
@login_required
def home(request):
    """用户登陆之后才能看home"""
    print(request.user)  # 用户对象     AnonymousUser匿名用户
    # 判断用户是否登陆
    print(request.user.is_authenticated())
    # 自动去django_session里面查找对应的用户对象给你封装到request.user中
    return HttpResponse('home')

"""
1.如果局部和全局都有 该听谁的?
    局部 > 全局
2.局部和全局哪个好呢?
    全局的好处在于无需重复写代码 但是跳转的页面却很单一
    局部的好处在于不同的视图函数在用户没有登陆的情况下可以跳转到不同的页面
"""
# @login_required(login_url='/login/')
@login_required
def index(request):
    return HttpResponse('index')


@login_required
def set_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        # 先校验两次密码是否一致
        if new_password == confirm_password:
            # 校验老密码对不对
            is_right = request.user.check_password(old_password)  # 自己加码比对密码
            if is_right:
                # 修改密码
                request.user.set_password(new_password)  # 仅仅是在修改对象的属性
                request.user.save()  # 这一步才是真正的操作数据库
        return redirect('/login/')

    return render(request,'set_password.html',locals())


@login_required
def logout(request):
    auth.logout(request)  # 类似于request.session.flush()
    return redirect('/login/')
from app01 import models

from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 操作auth_user表写入数据
        # User.objects.create(username=username,password=password)  # 写入数据  不能用create 密码没有加密处理
        # 创建普通用户
        # User.objects.create_user(username=username,password=password)
        # 创建超级用户(了解):使用代码创建超级用户 邮箱是必填的 而用命令创建则可以不填
        User.objects.create_superuser(username=username,email='123@qq.com',password=password)
    return render(request,'register.html')



