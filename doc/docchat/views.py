from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import connection
from datetime import datetime
from django.http import HttpResponse
import time
from django.http import HttpResponse
import datetime

from .models import doctor
# Create your views here.saz

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]
        # Check if username and password are correct, returning User object if so
        cursor=connection.cursor()
        cursor.execute('SELECT password FROM docchat_user WHERE username=(%s)',[username])
        pas = cursor.fetchone()
       # print(pas[0])
        connection.commit()
        connection.close()
        print(pas)  
        if password==pas[0]:
            #login(request, user)
            return HttpResponseRedirect(reverse("book"))
        else:
            return render(request, "user.html",{
                "message":"Invalid credentials"
            })
        #user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     #return render(request,'quiz.html')
        #     return HttpResponseRedirect(reverse("template"))
        #     # Otherwise, return login page again with new context
        # else:
        #     return render(request, "login.html", {
        #         "message": "Invalid Credentials"
        #     })
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html", {
                "message": "Logged Out"
            })

def doc(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]
        #print(fname)
        # Check if username and password are correct, returning User object if so
        doctor = authenticate(request, username=username, password=password)
        #print(doctor)
        if doctor is not None:
            login(request, doctor)
            #return render(request,'quiz.html')
            return HttpResponseRedirect(reverse("template"))
            # Otherwise, return login page again with new context
        else:
            return render(request, "login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "doctor.html")

def user(request):
    if request.method == "POST":
        username=request.POST["uname"]
        name=request.POST["name"]
        email=request.POST["mail"]
        password=request.POST["passw"]
        cursor=connection.cursor()
        cursor.execute('SELECT username FROM docchat_user WHERE username=(%s)',[username])
        ans = cursor.fetchone()
        if ans==None:
            cursor.execute('INSERT INTO docchat_user (username,name,email,password) VALUES (%s,%s,%s,%s)',[username,name,email,password])
            connection.commit()
            connection.close()  
            return HttpResponseRedirect(reverse("user"))
        else:
            return render(request, "sign.html",{
                "message":"Username already exists"
            })
    return render(request,'user.html')

def sign(request):
    return render(request,'sign.html')

def book(request):
    if request.method == "POST":
        spl = request.POST["spl"]
        return render(request,'book.html',{ "spl":spl, "doc":doctor.objects.all()})
    return render(request,'book.html',{ "doc":doctor.objects.all() })

def appointment(request):
    if 'instant' in request.POST:
        id = request.POST.get('instant')
        return render(request,'chat.html',{"id":id})
    elif 'later' in request.POST:
        id = request.POST.get('later')
        return render(request,'appointment.html',{"id":id,"doc":doctor.objects.all()})   
    return render(request,'appointment.html')

def chat(request):
    return render(request,'chat.html')

def billing(request):
    return render(request,'billing.html')

def lappointment(request):
    if request.method == "POST":
        Date=request.POST["date"]
        Time=request.POST["time"]
        cursor=connection.cursor()
        cursor.execute('INSERT INTO docchat_Lateappointment (Date,Time) VALUES (%s,%s)',[Date,Time])
        connection.commit()
