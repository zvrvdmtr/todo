from django.urls import path
from .views import TaskList, TaskView

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>', TaskView.as_view()),
]
