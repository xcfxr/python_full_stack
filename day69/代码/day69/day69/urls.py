"""day69 URL Configuration

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
    # 登陆功能
    url(r'^login/',views.login),
    url(r'^home/',views.home),
    url(r'^index/',views.index),
    url(r'^func/',views.func),
    # 注销功能
    url(r'^logout/',views.logout),

    # session操作
    url(r'^set_session/',views.set_session),
    url(r'^get_session/',views.get_session),
    url(r'^del_session/',views.del_session),

    # CBV添加装饰器
    url(r'^mylogin/',views.MyLogin.as_view())
]
