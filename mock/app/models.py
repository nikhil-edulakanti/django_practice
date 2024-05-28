from django.db import models

# Create your models here.
class user_input(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    text=models.TextField(max_length=1000)
