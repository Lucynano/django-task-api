from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

# handles GET requests to list all tasks and POST request to create new task
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# handles GET for one task, PUT/PATCH for updating and DELETE to remove a task
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
