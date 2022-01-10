"""mynewdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url

from django.shortcuts import HttpResponse
def index(request,id):
    print(id,type(id))
    return HttpResponse('index')
def login(request,xx):
    print(xx,type(xx))  # 113 <class 'str'>
    return HttpResponse('login')

class MonthConverter:
    regex='\d{2}' # 属性名必须为regex

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return value # 匹配的regex是两个数字，返回的结果也必须是两个数字



urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^index/',index),
    url(r'^login/(\d+)/',login),

    path('index/<int:id>/',index)
    # 将第二个路由里面的内容先转成整型然后以关键字的形式传递给后面的视图函数
]
