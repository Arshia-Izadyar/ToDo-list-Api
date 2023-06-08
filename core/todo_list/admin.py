from .models import TaskModel
from django.contrib.admin import register, ModelAdmin


@register(TaskModel)
class TaskModelAdmin(ModelAdmin):
    list_display = ('title', 'is_complete', 'dead_line', 'description', 'tags', 'user')
    list_filter = ('is_complete', )
    
