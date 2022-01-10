from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^reg/',views.reg,name='app01_reg'),
    # 三板斧
    url(r'^index/',views.index),
    # json相关
    url(r'^ab_json/',views.ab_json),
    # 上传文件
    url(r'^ab_file/',views.ab_file),
    # CBV路由
    url(r'^login/',views.MyLogin.as_view())
]