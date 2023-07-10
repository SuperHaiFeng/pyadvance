"""为learning_logs定义URL模式"""

from django.urls import path, include
from learning_logs import views

urlpatterns = [
    #默认首页是index.html（http://127.0.0.1:8000/）
    path('index/', views.index, name='index'),

    path('topics/', views.topics, name='topics'),

    #特定主题的详细页面
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #用于添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),

    #用于添加新条目的页面
    #这个URL模式与形式为http://localhost:8000/new_entry/id/的URL匹配，其中id是一个与主题ID匹配的数字。代码(?P<topic_id>\d+)捕获一个数字值，并将其存储在变量topic_id中。请求的URL与这个模式匹配时，Django将请求和主题ID发送给函数new_entry()。
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #编辑条目
    path(r'^edit_entry/(?P<topic_id>\d+)/$', views.edit_entry, name='edit_entry'),

]