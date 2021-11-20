from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, CategoryForm, TaskForm
from apps.app.models import Category, Task
from django.contrib.auth.models import User

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
            return redirect("home")
        data['form'] = form

    # sino entre como get normal
    return render(request, "registration/register.html", data)


def Tasks(request):
    # traigo todas las tareas de la db
    tasksList = Task.objects.all();
    return render(request, 'listTasks.html', { 'listTask': tasksList})


def addTask(request):
    formTask = TaskForm()
    #formTask.fields['owner'].queryset = User.objects.all().filter(is_superuser = False)
    print(formTask.fields)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        formTask['form'] = form

    return render(request, 'addTask.html', { 'form': formTask })

def deleteTask(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete();
    return redirect(to='tasks')

def updateTask(request,id):
    #buscar tarea veficando que exista
    task = get_object_or_404(Task,id=id)
    #creo el formulario y lo relleno con la tarea encontrada
    formTask = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        formTask['form'] = form


    return render(request, 'updateTask.html', { 'form': formTask })