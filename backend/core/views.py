from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Create your views here.


class TaskList(generics.ListCreateAPIView):

    queryset = Task.objects.all().order_by('-due_date')
    serializer_class = TaskSerializer


class TaskView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
