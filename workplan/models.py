from django.db import models
from datetime import date
# Create your models here.
class Todo(models.Model):
    """TODO MODEL"""
    PRIORITY=(
         (1, 'High'),
         (2, 'Medium'),
         (3, 'Low'),
        )
    TASK_STATUS=(
         (1, 'Todo'),
         (2, 'Doing'),
         (3, 'Done'),
        )
    name=models.CharField(max_length=100, help_text="Name of todo")
    description=models.CharField(max_length=200, help_text="description of todo")
    priority=models.IntegerField(choices=PRIORITY, default=2, help_text="Priority")
    task_status=models.IntegerField(choices=TASK_STATUS, default=1)
    due_date=models.DateField()
    def is_due(self):
        return date.today() > self.due_date
