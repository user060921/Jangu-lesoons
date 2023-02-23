from django.contrib import admin
from django.urls import path
from todo_list.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',register_page, name='register_page'),
    path('login/',login_page,name='login'),
    path('logout_page/',logout_user,name='logout'),
    path('task_list/',task_list,name='task_list'),
    path('create_task/',create_task,name='create_task'),
    path('delete_task/<int:pk>/',delete_task, name='delete_task'),
    path('update_task/<int:pk>/',update_task, name='update_task'),
]
   
