# from django.conf.urls import url
from django.urls import re_path as url

from . import views

# 导入 跟下面的找函数的对应的
from app01 import views
from django.contrib import admin

#ajax

 
urlpatterns = [
    # url(r'^$', views.hello),
    # 去app01 里面的views找这个index函数
    url('index/', views.index),
    url('about/', views.about),
    url('work/', views.work),
    url('contact/', views.contact),
    url('information/', views.information),

    url('history/', views.history),



    url('panel/', views.panel),
    url('test_form/', views.test_form),


    url('button2/', views.button2_html),
    url('button2_fx_ajax/', views.button2_fx_view),
    

    url('button3/', views.button3),


    url('test_map/', views.test_map),

    url('admin/', admin.site.urls),


    url('test_ajax/', views.test_ajax_html),
    url('test_ajax_fx/', views.test_ajax)





]