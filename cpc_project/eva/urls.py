from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.page404, name='404page'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]