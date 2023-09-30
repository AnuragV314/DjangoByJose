from typing import Any
from django.shortcuts import render

# from django.views import View 
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import *

# Create your views here.


# class CBView(View):
#     def get(self, request):
#         return render(request, 'index.html', {})


class IndexView(TemplateView):
    template_name = 'index.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION!.'
    #     return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'basic_app/school_detail.html'
    


