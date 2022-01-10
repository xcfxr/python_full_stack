from django.conf.urls import url
from app02 import views

urlpatterns = [
    url(r'^reg.html',views.reg,name='app02_reg')
]