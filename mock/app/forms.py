from django import forms
from django.core import validators
from app.models import user_input



class User(forms.ModelForm):
    name=forms.CharField(validators=[validators.MaxLengthValidator(20)])
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model=user_input
        fields="__all__"