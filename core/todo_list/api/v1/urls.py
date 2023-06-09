from django.urls import path
from .views import TaskView
# from rest_framework.routers import DefaultRouter



task_list = TaskView.as_view({
    'get': "list",
    'post': "create"
})

task_retrieve = TaskView.as_view({
    'get': "retrieve",
    'put': "update",
    "delete": "destroy"
})

# router = DefaultRouter()
# router.register('list', TaskView,basename="snippet")

urlpatterns = [
    path('task-list/', task_list, name='task-list'),
    path('task-detail/<int:pk>/', task_retrieve, name='task-detail'),
    
    # path('task-detail/<int:pk>/', TaskRetrieve.as_view(), name='task-detail'),
    # path('', include(router.urls)),
]
