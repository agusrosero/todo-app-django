from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
]
