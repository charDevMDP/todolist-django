from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login

from apps.app.models import Category

# Create your views here.

def home(request):
    return render(request, "home.html")

def Categories(request):
    # traigo todas las categorias de la db
    categoriesList = Category.objects.all();
    return render(request, 'listCategories.html', { 'listCat': categoriesList})

def addCategory(request):
    name = request.POST['catName'];
    category = Category.objects.create(name=name);
    return redirect('categories')

def addCategoryForm(request):
    categoriesList = Category.objects.all();
    return render(request, 'addCategory.html', { 'listCat': categoriesList})

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
