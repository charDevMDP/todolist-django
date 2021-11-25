from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name="register"),
    path('categories/', login_required(views.Categories), name='categories'),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('tasks/', login_required(views.Tasks), name='tasks'),
    path('addTasks/', views.addTask, name='addTask'),
    path('deleteTask/<id>/', views.deleteTask, name='deleteTask'),
    path('updateTask/<id>/', views.updateTask, name='updateTask'  )
]
