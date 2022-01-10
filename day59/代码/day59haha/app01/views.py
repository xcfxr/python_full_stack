from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    """
    :param request: 请求相关的所有数据对象 比你之前的env更加牛逼
    :return:
    """
    # return HttpResponse("你好啊 我是django妹纸")
    # return render(request,'myfirst.html')  # 自动去tempaltes文件夹下帮你查找文件
    # return redirect('https://www.mzitu.com/')
    return redirect('/home/')


def home(request):
    return HttpResponse('home')

