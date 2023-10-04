from django.urls import path
from .views import *

app_name = 'groups'

urlpatterns = [
    path('', ListGroups.as_view(), name='all'),
    path('new/', CreateGroup.as_view(), name='create'),
    path('posts/in/<slug>/', SingleGroup.as_view(), name='single'),
]


