from django.urls import path
from .views import TaskListCreate, TaskDetail

urlpatterns = [
    #route to access or create tasks
    path('tasks/', TaskListCreate.as_view(), name='task-list'),
    
    #route to get, update, or delete a single task by its primary key (pk)
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]