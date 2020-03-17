from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index/<int:p_id>/', views.detail),
    path('login/', views.login),
]