from django.urls import path, include
from todo import views
from django.contrib import admin


urlpatterns =[
    path('', views.todo, name='todo'),
    path('todolist/', views.todo, name='todo'),
    path('todolist/edit/<id>', views.edit, name='edit'),
    path('todolist/delete/<id>', views.delete, name='delete'),
]