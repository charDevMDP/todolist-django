from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm


# Create your views here.

def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            return redirect("home")
    else:
        return render(request, "registration/register.html")
