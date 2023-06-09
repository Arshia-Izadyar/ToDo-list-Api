from django.urls import path, include
from .views import TaskListAPIView, TaskRetrieve, TaskView
from rest_framework.routers import DefaultRouter



# task_list = TaskView.as_view({
#     'get': "list"
# })

router = DefaultRouter()
router.register('list', TaskView,basename="snippet")

urlpatterns = [
    # path('task-list/', task_list, name='task-list'),
    # path('task-detail/<int:pk>/', TaskRetrieve.as_view(), name='task-detail'),
    path('', include(router.urls)),
]
