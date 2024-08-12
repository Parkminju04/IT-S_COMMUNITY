from django.urls import path
from . import views

urlpatterns = [
    path('my_setting/', views.my_setting, name='my_setting'),
    path('join/', views.join, name='join'),
    # 다른 URL 패턴들
]