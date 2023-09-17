import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
django.setup()

#   it's importent to  import all after 'env' and 'setup()'
# https://stackoverflow.com/questions/26082128/improperlyconfigured-you-must-either-define-the-environment-variable-django-set#:~:text=Add%20a%20comment-,1,%22admin.settings%22)%0Adjango.setup()%0A%0Afrom%20products.models%20import%20Product,-Share

from faker import Faker
from first_app.models import Topic, Webpage, Access
import random

# FAKE POP SCRIPT


fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Game']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):
        # get the topic for entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #  Create a new webpage entry
        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]
        
        # create a fake access record for that webpage
        acc_rec = Access.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete.')




