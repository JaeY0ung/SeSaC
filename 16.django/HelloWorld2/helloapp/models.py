from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f'<{self}> {self.text}'
    
class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'<{self}> {self.title} {self.content}'

