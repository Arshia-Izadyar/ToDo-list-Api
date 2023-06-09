from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    
class TaskRetrieve(RetrieveUpdateDestroyAPIView):
    model = TaskModel
    queryset = TaskModel.objects
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class TaskView(ViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    
    def list(self, request):
        # query = 
        serializer = TaskSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass