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
class doctor(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    #default="hi"
    def __str__(self):
        return f" {self.username}"
class appointment(models.Model):
    #docname=models.CharField(max_length=50)
    #patID= models.OneToOneField('user',on_delete=models.CASCADE,blank=True)
    current_date=models.DateField(max_length=50)
    current_time=models.TimeField(max_length=50)
    
#class schedule(models.Model):
    



