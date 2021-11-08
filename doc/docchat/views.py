from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import connection

# Create your views here.

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]
        # Check if username and password are correct, returning User object if so
        cursor=connection.cursor()
        cursor.execute('SELECT password FROM docchat_user WHERE username=(%s)',[username])
        pas = cursor.fetchone()
        print(pas[0])
        connection.commit()
        connection.close()  
        if password==pas[0]:
            #login(request, user)
            return HttpResponseRedirect(reverse("template"))
        else:
            return render(request, "login.html",{
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

def template(request):
    return render(request,'template.html')

def doctor(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]
        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
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
        cursor.execute('INSERT INTO docchat_user (username,name,email,password) VALUES (%s,%s,%s,%s)',[username,name,email,password])
        connection.commit()
        connection.close()  
    return render(request,'user.html')

def sign(request):
    return render(request,'sign.html')


