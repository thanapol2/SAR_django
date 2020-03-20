from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('login/', views.login),
    path('upload/', views.upload, name='upload'),


    path('form/', views.person_form, name='person_insert'), # get and post req. for insert operation
    path('person_edit/<str:id>/', views.person_form, name='person_update'), # get and post req. for update operation
    path('person_del/<str:id>/', views.person_delete, name='person_del'),
    path('list/', views.person_list, name='person_list'), # get req. to retrieve and display all records
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)