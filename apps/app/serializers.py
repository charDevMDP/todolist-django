from django.db.models import fields
from rest_framework import serializers
from .models import Category, Task
from django.contrib.auth.models import User

#class TaskSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Task
#        fields = ['title', 'description', 'create_at', 'state', 'url']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']
        
class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    print(owner)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['title', 'description', 'create_at', 'state', 'owner','category']