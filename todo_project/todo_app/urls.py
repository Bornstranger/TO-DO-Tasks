from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo_item, name='add_todo_item'),
    path('update/<int:pk>/', views.update_todo_item, name='update_todo_item'),
    path('delete/<int:pk>/', views.delete_todo_item, name='delete_todo_item'),
]
