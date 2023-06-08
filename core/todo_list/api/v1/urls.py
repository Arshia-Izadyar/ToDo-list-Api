from django.urls import path
from .views import TaskListAPIView, TaskRetrieve


urlpatterns = [
    path('task-list/', TaskListAPIView.as_view(), name='task-list'),
    path('task-detail/<int:pk>/', TaskRetrieve.as_view(), name='task-detail'),
]
