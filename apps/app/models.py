from django.db import models
from django.contrib.auth.models import User

options_state = [
    [0, 'por hacer'],
    [1, 'en curso'],
    [2, 'hecho']
]

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name


class Task(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.PROTECT, null=False)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    create_at=models.DateTimeField(auto_now_add=True)
    state=models.IntegerField(choices=options_state)

    def __str__(self):
        return self.title