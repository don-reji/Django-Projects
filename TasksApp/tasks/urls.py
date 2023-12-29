from django.urls import path
from .views import TaskDetailView,TasksListView

urlpatterns=[
    path('tasks/',TasksListView.as_view(),name='tasks-list'),
    path('tasks/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),
]