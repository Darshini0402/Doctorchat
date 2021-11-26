from django.core.checks import messages
from django.shortcuts import render,redirect
from . import models
from dchat.models import Room,Message
from django.http import HttpResponse, JsonResponse
from docchat.models import doctor

def home(request):
    return render(request, 'home.html')

def room(request, room):
    if 'instantapp' in request.POST:
        global dun
        dun = request.POST.get('instantapp')
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html',{
        'username':username, 'room':room, 'room_details': room_details
    })

def checkview(request):
    room=request.POST['room_name']
    username=request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    #messages = Message.objects.filter(room_icontains = room)
    messages = Message.objects.filter(room = room_details.id)

    return JsonResponse({"messages":list(messages.values())})

def billing(request):
    return render(request,'billing.html',{"un":dun,"doc":doctor.objects.all()})