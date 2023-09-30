from django.urls import path
from .views import *

app_name = 'basic_app'

urlpatterns=[
    path('', SchoolListView.as_view(), name='list'),
    path('<int:pk>', SchoolDetailView.as_view(), name='detail'),
    
]