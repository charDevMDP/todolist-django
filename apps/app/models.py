from django.db import models
from django.contrib.auth.models import User

options_state = [
    ('Por Hacer', 'por hacer'),
    ('En Curso', 'en curso'),
    ('Hecho', 'hecho')
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
    owner=models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='tasks')
    create_at=models.DateTimeField(auto_now_add=True)
    state=models.CharField(max_length=15,choices=options_state)

    def __str__(self):
        return self.title