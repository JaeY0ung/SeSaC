from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'title: {self.title}, completed: {self.completed}'