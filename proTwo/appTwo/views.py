from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    my_dict={"insert":"This is from views.py"}
    return render(request,"appTwo/index.html",context=my_dict)

def page(request):
    return HttpResponse("new page")

def users(request):
    users_list=User.objects.all()
    dict={"users":users_list}
    return render(request,"appTwo/users.html",context=dict)