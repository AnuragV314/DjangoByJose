from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    return render(request, 'basic_app/registration.html', {})


def user_login(request):
    return render(request, 'basic_app/login.html', {})