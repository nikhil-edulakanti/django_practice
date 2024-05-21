from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns=[
    path("",views.index,name="index"),
    path("second/",views.page,name="Second"),
    path("users/",views.users,name="Users")
]