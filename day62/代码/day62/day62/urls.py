"""day62 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

# from app01 import urls as app01_urls
# from app02 import urls as app02_urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 首页
    # url(r'^$', views.home),
    # # 无名分组反向解析
    # url(r'^index/(\d+)/',views.index,name='xxx'),
    # # 有名分组反向解析
    # url(r'^func/(?P<year>\d+)/',views.func,name='ooo')

    # 路由分发
    # url(r'^app01/',include(app01_urls)),  # 只要url前缀是app01开头 全部交给app01处理
    # url(r'^app02/',include(app02_urls))   # 只要url前缀是app02开头 全部交给app02处理
    # 终极写法  推荐使用
    # url(r'^app01/',include('app01.urls',namespace='app01')),
    # url(r'^app02/',include('app02.urls',namespace='app02'))
    # 注意事项:总路由里面的url千万不能加%结尾

    url(r'^app01/', include('app01.urls')),
    url(r'^app02/', include('app02.urls')),



]
"""
index/数字/

reverse('xxx')  报错 你还需要指定一个参数能够被\d+匹配到
index/1/
index/11/
index/123/
...

reverse('ooo')
func/1/
func/12/
func/1324/

"""
