from rest_framework import serializers
from django.contrib.auth.models import User
from todo_list.models import TaskModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "id")


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TaskModel
        fields = (
            "id",
            "user",
            "title",
            "description",
            "is_complete",
            "tags",
            "dead_line",
            "tags",
        )
        read_only_fields = ("id", "user")

    # def to_representation(self, instance):
    #     request = self.context.get('request')
    #     rep = super().to_representation(instance)

    #     if not request.parser_context['kwargs']:
    #         rep.pop('description')
    #     return rep
