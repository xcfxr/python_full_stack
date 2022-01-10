"""day61 URL Configuration

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
    # 首页
    url(r'^$',views.home),
    # 路由匹配
    # url(r'^test/(\d+)/',views.test),
    # url(r'^testadd/$',views.testadd),
    # 尾页(了解)
    # url(r'',views.error),
    # 无名分组
    url(r'^test/(\d+)/',views.test),
    # 有名分组
    url(r'^testadd/(?P<year>\d+)',views.testadd),
    # 无名有名混用  不能混用！！！
    # url(r'^index/(\d+)/(?P<year>\d+)/',views.index),
    # 单个的分组可以使用多次
    url(r'^index/(\d+)/(\d+)/(\d+)/',views.index),
    url(r'^index/(?P<year>\d+)/(?P<age>\d+)/(?P<month>\d+)/',views.index),

    # 反向解析
    url(r'^func_kkkyyyy/',views.func,name='ooo')

]
