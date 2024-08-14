from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('my_setting/', views.my_setting, name='my_setting'),
    path('join/', views.join, name='join'),
    # 다른 URL 패턴들
]
