"""day63 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # CBV
    # url(r'^login/',views.MyLogin.as_view()),
    # 上述代码在启动django的时候就会立刻执行as_view方法
    # url(r'^login/',views.view)  FBV一模一样
    # CBV与FBV在路由匹配上本质是一样的 都是路由 对应 函数内存地址

    # 模版语法传值
    url(r'^index/',views.index),

    # 模版的继承
    url(r'^home/',views.home),
    url(r'^login/',views.login),
    url(r'^reg/',views.reg),
]
"""
函数名/方法名 加括号执行优先级最高
猜测
    as_view()
        要么是被@staicmethod修饰的静态方法
        要么是被@classmethod修饰的类方法  正确
        
    @classonlymethod
    def as_view(cls, **initkwargs):
        pass
"""
