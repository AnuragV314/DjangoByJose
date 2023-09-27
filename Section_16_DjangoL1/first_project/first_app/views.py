from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# HttpResponse==>

# def index(request):
#     return HttpResponse('Hello World!')


#  render==>

# def index(request):
#     return render(request, 'index.html', {})


def index(request):
    my_dict = {'insert_me':'Hello I am from views.py! (first_app/index.html)'}
    return render(request, 'first_app/index.html', context=my_dict)
