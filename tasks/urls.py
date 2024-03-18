from django.urls import path
from .views import index, task_list, TaskDetailView, TaskListView

urlpatterns = [
    path('', index, name = 'index'),
    # path('list', task_list, name = 'list'),
    path('list', TaskListView.as_view(), name = 'list'),
    path('<int:pk>/detail', TaskDetailView.as_view(), name='task_detail')
]

app_name = 'tasks'

