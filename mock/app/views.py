from django.shortcuts import render
from .forms import User

# Create your views here.
def home(request):
    my_dict={"insert":"SUP GGGG THIS IS HOME"}
    return render(request,"app/home.html",context=my_dict)


def help(request):
    my_dict={"insert":"SUP G"}
    return render(request,"app/help.html",context=my_dict)

def user_view(request):
    form=User()
    my_dict={"forms":form}
    if request.method=="POST":
        form=User(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCES")
            print("1:" + form.cleaned_data["name"])
            print("2:" + form.cleaned_data["email"])
            print("3:" + form.cleaned_data["text"])

        else:
            print("Invalid form")
    return render(request,"app/forms.html",context=my_dict)