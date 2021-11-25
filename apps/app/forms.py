from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Category, Task


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]
        help_texts = {k:'' for k in fields}

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']
        #fields = '__all__'
        labels = { 'name': ('Nombre de la categoria'), 'description': ('Breve descripcion')}
        help_texts = {k:'' for k in fields}


class TaskForm(forms.ModelForm):
    title = forms.CharField(label='Titulo')
    description = forms.CharField(label='Descripcion')
    #category = forms.ChoiceField(label='Seleccione una categoria',widget=forms.Select)
    #state = forms.ChoiceField(label='Elige el estado inicial de la tarea')
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'state' ]
        help_texts = {k: '' for k in fields}