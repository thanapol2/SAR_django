from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.page404, name='404page'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('sub_category1/', views.sub_category1, name='subcate1'),
    path('add_subcate11/', views.add_form_no11, name='add_form_no11'),

    path('sub_category2/', views.sub_category2, name='subcate2'),
    path('sub_category3/', views.sub_category3, name='subcate3'),
    path('sub_category4/', views.sub_category4, name='subcate4'),
    path('sub_category5/', views.sub_category5, name='subcate5'),
]