from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('formpage/', form_name_view)
]