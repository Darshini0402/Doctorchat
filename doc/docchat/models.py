from django.db import models
from django.db.models.fields import related
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=10)
    # repassword=models.CharField(max_length=10)
    def __str__(self):
        return f" {self.username}"


