from django.urls import path
from .views import *

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('other/', other, name='other'),
    path('relative/', relative, name='relative'),

]