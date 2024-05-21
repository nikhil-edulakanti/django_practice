from django import forms
from django.core import validators


def check_x(value):
    if value[0].lower!="x":
        raise forms.ValidationError("start with x")

class User(forms.Form):
    name=forms.CharField(validators=[check_x])
    email=forms.EmailField()
    verif_email=forms.EmailField(label="enter email again")
    text=forms.CharField(widget=forms.Textarea)