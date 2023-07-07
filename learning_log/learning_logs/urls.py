"""为learning_logs定义URL模式"""

from django.urls import path, include
from learning_logs import views

urlpatterns = [
    #默认首页是index.html（http://127.0.0.1:8000/）
    path('index/', views.index, name='index'),

    path('topics/', views.topics, name='topics'),

    #特定主题的详细页面
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]