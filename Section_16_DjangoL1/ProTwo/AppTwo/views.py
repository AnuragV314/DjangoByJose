from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    helpdict = {'help_page':'heloo page from views.py'}
    return render(request, 'AppTwo/help.html', context=helpdict)