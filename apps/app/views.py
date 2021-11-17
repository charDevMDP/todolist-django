from django.shortcuts import redirect, render

from django.contrib.auth.views import LoginView

from apps.app.models import Category

# Create your views here.

def home(request):
    return render(request, "home.html")

def Categories(request):
    categoriesList = Category.objects.all();
    return render(request, 'listCategories.html', { 'listCat': categoriesList})

def addCategory(request):
    name = request.POST['catName'];
    category = Category.objects.create(name=name);
    return redirect('categories')

def addCategoryForm(request):
    categoriesList = Category.objects.all();
    return render(request, 'addCategory.html', { 'listCat': categoriesList})
