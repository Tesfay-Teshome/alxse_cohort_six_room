from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Room, Topic, Message
from .forms import RoomForm

# Create your views here.
# rooms = [
#     {'id': 1, 'name': 'Lets Learn Python'},
#     {'id': 2, 'name': 'Lets Learn Django'},
#     {'id': 3, 'name': 'Lets Learn Javascript'},
#     {'id': 4, 'name': 'Lets Learn React'},
#     {'id': 5, 'name': 'Lets Learn Vue'},
#     {'id': 6, 'name': 'Lets Learn Angular'},
#     {'id': 7, 'name': 'Lets Learn Node'},
# ]
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms }
    return render(request, "base/home.html", context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, "base/room.html", context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
                            
                            
                            