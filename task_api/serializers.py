from rest_framework import serializers
from .models import Task

# Serializers turn Django model into JSON
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'