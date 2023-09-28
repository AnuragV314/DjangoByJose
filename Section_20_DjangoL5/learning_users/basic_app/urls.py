from django.urls import path
from .views import *

# TEMPLATES URLS
app_name = "basic_app"

urlpatterns= [
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
]