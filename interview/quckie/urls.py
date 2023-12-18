from django.urls import path
from quckie import views

urlpatterns =[
    path('tasks/',views.task_list,name='tasks'),
    path('task/<int:pk>/',views.task_detail,name='task_detail'),
]