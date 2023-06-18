from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters

from todo_list.models import TaskModel
from .serializer import TaskSerializer



class TaskListAPIView(ListCreateAPIView):
    model = TaskModel
    queryset = TaskModel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ("tags", "is_complete")
    search_fields = ("title",)
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

"""
class TaskRetrieve(RetrieveUpdateDestroyAPIView):
    model = TaskModel
    queryset = TaskModel.objects
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
"""

class TaskView(ViewSet):
    model = TaskModel
    permission_classes = (IsAuthenticated,)
    queryset = TaskModel.objects
    serializer_class = TaskSerializer


    # def list(self, request):
    #     query = self.queryset.filter(user=self.request.user)
    #     serializer = self.serializer_class(query, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    


    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(user = self.request.user)
    #     return Response({"Status": "Created"}, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj.user == self.request.user:
            serialized = self.serializer_class(obj).data
            return Response(serialized, status=status.HTTP_200_OK)
        else:
            return Response({"Status": "Not authenticated for this task"}, status=status.HTTP_403_FORBIDDEN)
        

    def update(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)

        if obj.user == self.request.user:
            serialized = self.serializer_class(obj, request.data)
            serialized.is_valid(raise_exception=True)
            serialized.save()
            return Response({"Status": "Updated", "data": serialized.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"Status": "Not authenticated for this task"}, status=status.HTTP_403_FORBIDDEN)


    def destroy(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)

        if obj.user == self.request.user:
            obj.delete()
            return Response({"Status": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"Status": "Not authenticated for this task"}, status=status.HTTP_403_FORBIDDEN)
