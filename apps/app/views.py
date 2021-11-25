from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, CategoryForm, TaskForm
from apps.app.models import Category, Task
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import routers, serializers, viewsets, generics
from .serializers import TaskSerializer, UserSerializer

from rest_framework.views import exception_handler

# Create your views here.

def home(request):
    return render(request, "home.html")

def Categories(request):
    # traigo todas las categorias de la db
    categoriesList = Category.objects.all();
    return render(request, 'listCategories.html', { 'listCat': categoriesList})


def addCategory(request):
    data = { 'form': CategoryForm()}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Categoria creada correctamente')
            return redirect('categories')
        data['form'] = form

    return render(request, 'addCategory.html', data)


def register(request):
    data = { 'form': UserRegisterForm() }
    # si entra con el metodo POST
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # guardo en la db
            form.save()
            # authenticar manualmente
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            # inicio sesion usuario
            login(request, user)
            messages.success(request, f'Usuario {username} creado correctamente')
            return redirect("home")
        data['form'] = form

    # sino entre como get normal
    return render(request, "registration/register.html", data)


def Tasks(request):
    # guardo usuario actual
    current_user = request.user
    # accedo a todas la tareas de ese usuario
    tasksList = current_user.tasks.all()

    # traigo todas las tareas de la db - antes
    #tasksList = Task.objects.all(); - antes ahora traigo solo los del usuario

    return render(request, 'listTasks.html', { 'listTask': tasksList})


def addTask(request):
    formTask = TaskForm()
    #verificar si hay usuario y la guardo para configurarselo a la tarea 
    current_user = get_object_or_404(User, pk=request.user.pk)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # commit falso, porque hay que config el usuario owner
            task = form.save(commit=False)
            # asignamos el usuario logueado a la tarea
            task.owner = current_user
            task.save()
            messages.success(request, f'Tarea creada correctamente')
            return redirect('tasks')
        formTask['form'] = form

    return render(request, 'addTask.html', { 'form': formTask })

def deleteTask(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete();
    messages.success(request, f'Tarea eliminada correctamente')
    return redirect(to='tasks')

def updateTask(request,id):
    #buscar tarea veficando que exista
    task = get_object_or_404(Task,id=id)
    #creo el formulario y lo relleno con la tarea encontrada
    formTask = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea editada correctamente')
            return redirect('tasks')
        formTask['form'] = form


    return render(request, 'updateTask.html', { 'form': formTask })

# making an api

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ['owner__username']
    
class UserListSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
