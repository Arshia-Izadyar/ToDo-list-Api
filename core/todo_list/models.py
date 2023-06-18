from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    WORK = 1
    SCHOOL = 2
    PERSONAL = 3
    URGENT = 4
    TRAVEL = 5
    SOCIAL = 6
    FAMILY = 7
    DEADLINES = 8
    GOALS = 9

    tags = (
        (WORK, "Work"),
        (SCHOOL, "School"),
        (PERSONAL, "Personal"),
        (URGENT, "urgent"),
        (TRAVEL, "travel"),
        (SOCIAL, "social"),
        (FAMILY, "Family"),
        (DEADLINES, "deadlines"),
        (GOALS, "goals"),
    )

    title = models.CharField(max_length=35)
    is_complete = models.BooleanField(default=False)
    dead_line = models.DateField()
    description = models.TextField(blank=True, null=True)
    tags = models.PositiveSmallIntegerField(choices=tags, default=WORK)
    user = models.ForeignKey(User, related_name="Tasks", on_delete=models.PROTECT)

    def __str__(self):
        return self.title
