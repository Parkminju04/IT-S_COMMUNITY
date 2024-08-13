from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('my_setting/', views.my_setting, name='my_setting'),
    path('join/', views.join, name='join'),
    path('login/', auth_views.LoginView.as_view(template_name='login_error.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
