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

from .models import doctor, patappointment,user
# Create your views here.saz

def login_view(request):
    global uusername
    if request.method == "POST":
        # Accessing username and password from form data
        global uusername
        uusername = request.POST.get("username")
        upassword = request.POST.get("password")
        # Check if username and password are correct, returning User object if so
        cursor=connection.cursor()
        cursor.execute('SELECT password FROM docchat_user WHERE username=(%s)',[uusername])
        pas = cursor.fetchone()
       # print(pas[0])
        connection.commit()
        connection.close()  
        if pas == None:
            return render(request, "user.html",{
                "message":"User does not exist"
            })
        elif upassword==pas[0]:
            #login(request, user)
            return HttpResponseRedirect(reverse("option"))
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

def option(request):
    # if request.method == "POST":
    #     op = request.POST["option"]
    #     if op=="appoint":
    #         return render(request,'book.html')
    #     elif op=="edit":
    #         return render(request,'edit.html')
    #     elif op=="cancel":
    #         return render(request,"cancel.html")
    return render(request,'option.html')

def edit(request):
    return render(request,'edit.html',{"appointment":patappointment.objects.all(),"user":uusername,"doc":doctor.objects.all()})

def cancel(request):
    return render(request,'cancel.html',{"appointment":patappointment.objects.all(),"user":uusername,"doc":doctor.objects.all()})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {
                "message": "Logged Out"
            })

def doc(request):
    global dusername
    if request.method == "POST":
        # Accessing username and password from form data
        dusername = request.POST["username"]
        dpassword = request.POST["password"]
        # Check if username and password are correct, returning User object if so
        cursor=connection.cursor()
        cursor.execute('SELECT password FROM docchat_doctor WHERE username=(%s)',[dusername])
        pas = cursor.fetchone()
       # print(pas[0])
        connection.commit()
        connection.close()  
        if pas == None:
            return render(request, "user.html",{
                "message":"User does not exist"
            })
        elif dpassword==pas[0]:
            #login(request, user)
            return HttpResponseRedirect(reverse("template"))
        else:
            return render(request, "user.html",{
                "message":"Invalid credentials"
            })
    return render(request, "doctor.html")
    # if request.method == "POST":
    #     # Accessing username and password from form data
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     #print(fname)
    #     # Check if username and password are correct, returning User object if so
    #     doctor = authenticate(request, username=username, password=password)
    #     #print(doctor)
    #     if doctor is not None:
    #         login(request, doctor)
    #         #return render(request,'quiz.html')
    #         return HttpResponseRedirect(reverse("template"))
    #         # Otherwise, return login page again with new context
    #     else:
    #         return render(request, "login.html", {
    #             "message": "Invalid Credentials"
    #         })
    # return render(request, "doctor.html")

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
    global unl
    if 'instant' in request.POST:
        un = request.POST.get('instant')
        return render(request,'home.html',{"un":un})
        #return HttpResponseRedirect(reverse("chat"),{"un":un})
    elif 'later' in request.POST:
        global unl
        unl = request.POST.get('later')
        return render(request,'appointment.html',{"un":unl, "doc":doctor.objects.all()})   
    # return render(request,'appointment.html')


def billing(request):
    if request.method == "POST":
        pname = request.POST.get('inputname')
        page = request.POST.get('inputage')
        paadhar = request.POST.get('inputaadhar')
        pphone = request.POST.get('inputphone')
        psymptoms = request.POST.get('inputSymptoms')
        Date=request.POST.get("inputDate")
        Time=request.POST.get("inputTime")
        cursor=connection.cursor()
        cursor.execute('INSERT INTO docchat_patappointment (pname,page,paadhar,pphone,Date,Time,psymptoms,duname_id,uuname_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',[pname,page,paadhar,pphone,Date,Time,psymptoms,unl,uusername])
        connection.commit()
    # elif 'instantapp' in request.POST:
    #     dun = request.POST.get('instantapp')
    #     return render(request,'billing.html',{"un":dun,"doc":doctor.objects.all()})
    return render(request,'billing.html',{"un":unl, "doc":doctor.objects.all()})

def template(request):
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S", t)
    # current_date = datetime.date.today()
    # cursor=connection.cursor()
    # cursor.execute('INSERT INTO docchat_appointment (Time,Date) VALUES (%s,%s)',[current_time,current_date])
    # connection.commit()
    # connection.close() 
    if 'docinstant' in request.POST:
        return render(request,'home.html')
    return render(request,'template.html',{"appointment":patappointment.objects.all(),"doc":dusername})

def feedback(request):
    return render(request,'feedback.html')
