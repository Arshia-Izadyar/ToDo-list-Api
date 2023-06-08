from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from todo_list.models import TaskModel
from .serializer import TaskSerializer

class TaskListAPIView(ListCreateAPIView):
    model = TaskModel
    queryset = TaskModel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
    
class TaskRetrieve(RetrieveUpdateDestroyAPIView):
    model = TaskModel
    queryset = TaskModel.objects
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
    
    def get_object(self):
        obj = super().get_object()
        obj.user = self.request.user
        return obj