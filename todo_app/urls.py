from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
]
