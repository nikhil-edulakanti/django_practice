import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","proTwo.settings")

import django
django.setup()


import random
from appTwo.models import AccessRecord,Topic,Webpage,User
from faker import Faker

fakegen=Faker()
topics=["Search","Social","Marketplace","News","Games"]

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N):
    for entry in range(N):
        top=add_topic()

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()


        webpg=Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0] 

        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

def populateUser(N):
    for entry in range(N):
        fake_fname=fakegen.first_name()
        fake_lname=fakegen.last_name()
        fake_email=fakegen.email()

        user=User.objects.get_or_create(fname=fake_fname,lname=fake_lname,email=fake_email)[0]  

if __name__=="__main__":
    print("populating scrfipt")
    populateUser(25)
    print("complete")