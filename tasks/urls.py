from django.urls import path
from .views import (
    index, task_list, TaskDetailView, TaskListView, 
    TaskCreateView, TaskUpdateView
)

urlpatterns = [
    path('', index, name = 'index'),
    # path('list', task_list, name = 'list'),
    path('list', TaskListView.as_view(), name = 'list'),
    path('<int:pk>/detail', TaskUpdateView.as_view(), name='task_detail'),
    path('create', TaskCreateView.as_view(), name = 'create'),
]

app_name = 'tasks'

