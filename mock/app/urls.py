from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("help/",views.help,name="help"),
    path("forms/",views.user_view,name="user_form")
]
