from django.shortcuts import render, HttpResponse
from .models import User
# Create your views here.

def index(request):
    return render(request, 'AppTwo/index.html', {})


def users(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users': users_list}
    return render(request, 'AppTwo/users.html', context=user_dict)






