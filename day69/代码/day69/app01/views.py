from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


# 校验用户是否登陆的装饰器
"""
用户如果在没有登陆的情况下想访问一个需要登陆的页面
那么先跳转到登陆页面 当用户输入正确的用户名和密码之后
应该跳转到用户之前想要访问的页面去 而不是直接写死
"""
def login_auth(func):
    def inner(request,*args,**kwargs):
        # print(request.path_info)
        # print(request.get_full_path())  # 能够获取到用户上一次想要访问的url
        target_url = request.get_full_path()
        if request.COOKIES.get('username'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/login/?next=%s'%target_url)
    return inner

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'jason' and password == '123':

            # 获取用户上一次想要访问的url
            target_url = request.GET.get('next')  # 这个结果可能是None
            if target_url:
                obj = redirect(target_url)
            else:
                # 保存用户登陆状态
                obj = redirect('/home/')
            # 让浏览器记录cookie数据
            obj.set_cookie('username', 'jason666')
            # 超时时间3秒到期
            """
            浏览器不单单会帮你存
            而且后面每次访问你的时候还会带着它过来
            """
            # 跳转到一个需要用户登陆之后才能看的页面
            return obj
    return render(request,'login.html')


@login_auth
def home(request):
    # 获取cookie信息 判断你有没有
    # if request.COOKIES.get('username') == 'jason666':
    #     return HttpResponse("我是home页面，只有登陆的用户才能进来哟~")
    # # 没有登陆应该跳转到登陆页面
    # return redirect('/login/')
    return HttpResponse("我是home页面，只有登陆的用户才能进来哟~")


@login_auth
def index(request):
    # 获取cookie信息 判断你有没有
    # if request.COOKIES.get('username') == 'jason666':
    #     return HttpResponse("我是home页面，只有登陆的用户才能进来哟~")
    # # 没有登陆应该跳转到登陆页面
    # return redirect('/login/')
    return HttpResponse("我是index页面，只有登陆的用户才能进来哟~")


@login_auth
def func(request):
    # 获取cookie信息 判断你有没有
    # if request.COOKIES.get('username') == 'jason666':
    #     return HttpResponse("我是home页面，只有登陆的用户才能进来哟~")
    # # 没有登陆应该跳转到登陆页面
    # return redirect('/login/')
    return HttpResponse("我是func页面，只有登陆的用户才能进来哟~")


@login_auth
def logout(request):
    obj = redirect('/login/')
    obj.delete_cookie('username')
    return obj


def set_session(request):
    request.session['hobby'] = 'girl'
    # request.session['hobby1'] = 'girl1'
    # request.session['hobby2'] = 'girl2'
    # request.session['hobby3'] = 'girl3'
    # request.session.set_expiry()
    """
    内部发送了那些事
        1.django内部会自动帮你生成一个随机字符串
        2.django内部自动将随机字符串和对应的数据存储到django_session表中
            2.1先在内存中产生操作数据的缓存
            2.2在响应结果django中间件的时候才真正的操作数据库
        3.将产生的随机字符串返回给客户端浏览器保存
    """
    return HttpResponse('嘿嘿嘿')


def get_session(request):
    # print(request.session.get('hobby'))
    if request.session.get('hobby'):
        print(request.session)
        print(request.session.get("hobby"))
        print(request.session.get("hobby1"))
        print(request.session.get("hobby2"))
        print(request.session.get("hobby3"))

        """
        内部发送了那些事
            1.自动从浏览器请求中获取sessionid对应的随机字符串
            2.拿着该随机字符串去django_session表中查找对应的数据
            3.
                如果比对上了 则将对应的数据取出并以字典的形式封装到request.session中
                如果比对不上 则request.session.get()返回的是None
        
        """
        return HttpResponse("哈哈哈")
    return HttpResponse("大爷 关门了 明晚再来吧")


def del_session(request):
    request.session.delete()
    return HttpResponse('删喽')



from django.views import View
from django.utils.decorators import method_decorator
"""
CBV中django不建议你直接给类的方法加装饰器
无论该装饰器能都正常给你 都不建议直接加
"""

@method_decorator(login_auth,name='get')  # 方式2(可以添加多个针对不同的方法加不同的装饰器)
@method_decorator(login_auth,name='post')
class MyLogin(View):
    @method_decorator(login_auth)  # 方式3:它会直接作用于当前类里面的所有的方法
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)
    # @method_decorator(login_auth)  # 方式1:指名道姓
    def get(self,request):
        return HttpResponse("get请求")

    def post(self,request):
        return HttpResponse('post请求')









