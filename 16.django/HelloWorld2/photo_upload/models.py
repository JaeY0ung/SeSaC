from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')

    def __str__(self) -> str:
        return f'{self.title}, {self.image}'
    