from django.urls import path
from .views import index, TaskDetailView, TaskListView

urlpatterns = [
    path('', index, name = 'index'),
    path('list', TaskListView.as_view(), name = 'list'),
    path('<int:pk>/detail', TaskDetailView.as_view(), name='task_detail')
]

app_name = 'tasks'

