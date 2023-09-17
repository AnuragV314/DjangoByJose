from django.shortcuts import render
from .models import Topic, Webpage, Access

# Create your views here.
def index(request):
    webpages_list = Access.objects.order_by('date')
    date_dict = {'access_record': webpages_list}
    my_dict = {'insert_me': 'HELLO I AM FROM FIRSTAPP!'}
    return render(request, 'first_app/index.html', context=date_dict)






