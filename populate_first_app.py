import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

##Fake Pop Script
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker
print("Starting D")
fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']
print("Starting E")
def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t
print("Starting F")
def populate(N=5):

    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake access record for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
print("Starting X1")
if __name__ == '__main__':
        print("Populating Script!")
        populate(20)
        print("Populating Complete!")
print("Starting Z")
