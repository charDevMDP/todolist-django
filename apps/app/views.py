from django.shortcuts import render

from django.contrib.auth.views import LoginView

# Create your views here.

def home(request):
    return render(request, "home.html")
