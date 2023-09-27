from django.shortcuts import render
from .forms import FormName

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html', {})


def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print('validation data success')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])


    return render(request, 'basicapp/form_page.html', {'form': form})

