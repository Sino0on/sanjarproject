from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', index, name='home'),
    path('detail/<int:pk>', detail, name='detail'),
    path('register/', register, name='registerPage'), # регистрация
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'), # авторизация
    path('logout/', auth_view.LogoutView.as_view(template_name='employer/logout.html'), name='logout'), # выйти
    path('create/post', postcreate, name='postcreate'),
    path('delety/<int:pk>', delety, name='delety')
]
