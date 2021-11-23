from django.db import models
from django.db.models.fields import related
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=10)
    # repassword=models.CharField(max_length=10)
    def __str__(self):
        return f" {self.username}"

class doctor(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    fee = models.IntegerField()
    city = models.CharField(max_length=64)
    exp = models.IntegerField()
    lang = models.CharField(max_length=250)
    spl = models.CharField(max_length=4)
    #default="hi"
    def __str__(self):
        return f" {self.fname}"

class patappointment(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    page = models.IntegerField()
    paadhar = models.CharField(max_length=20)
    pphone = models.PositiveBigIntegerField()
    Date=models.DateField(max_length=50)
    Time=models.TimeField(max_length=50)
    psymptoms = models.CharField(max_length=640)
    duname = models.ForeignKey(doctor, on_delete=models.CASCADE, related_name='duname')
    uuname = models.ForeignKey(user, on_delete=models.CASCADE, related_name='uuname')

    def __str__(self):
        return f" {self.pid}"