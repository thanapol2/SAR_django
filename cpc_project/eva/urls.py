from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.page404, name='404page'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('sub_category1/', views.sub_category1_Insert, name='subcate1'),
    path('update_sub_category1/', views.sub_category1_Update, name='update_sub_category1'),

    path('sub_category2/', views.sub_category2_Insert, name='subcate2'),
    path('update_sub_category2/', views.sub_category2_Update, name='update_sub_category2'),

    path('sub_category3/', views.sub_category3_Insert, name='subcate3'),
    path('update_sub_category3/', views.sub_category3_Update, name='update_sub_category3'),

    path('sub_category4/', views.sub_category4_Insert, name='subcate4'),
    path('update_sub_category4/', views.sub_category4_Update, name='update_sub_category4'),

    path('sub_category5/', views.sub_category5_Insert, name='subcate5'),
    path('update_sub_category5/', views.sub_category5_Update, name='update_sub_category5'),
]