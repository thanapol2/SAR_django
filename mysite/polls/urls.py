from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),

    path('form/', views.person_form, name='person_insert'), # get and post req. for insert operation
    path('person_edit/<str:id>/', views.person_form, name='person_update'), # get and post req. for update operation
    path('person_del/<str:id>/', views.person_delete, name='person_del'), # get and post req. for update operation
    path('list/', views.person_list, name='person_list'), # get req. to retrieve and display all records
]