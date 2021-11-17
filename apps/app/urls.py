from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.Categories, name='categories'),
    path('addCategory/', views.addCategoryForm, name='addCategory'),
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
]
