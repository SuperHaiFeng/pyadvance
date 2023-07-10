"""为应用程序users定义URL模式"""

from django.urls import path, include
from users import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    #登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 登出
    path('logout/', views.logout_view, name='logout'),
    #注册用户
    path('register/', views.register, name='register'),

]