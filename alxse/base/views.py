from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Lets Learn Python'},
    {'id': 2, 'name': 'Lets Learn Django'},
    {'id': 3, 'name': 'Lets Learn Javascript'},
    {'id': 4, 'name': 'Lets Learn React'},
    {'id': 5, 'name': 'Lets Learn Vue'},
    {'id': 6, 'name': 'Lets Learn Angular'},
    {'id': 7, 'name': 'Lets Learn Node'},
]
def home(request):
    context = {'rooms': rooms }
    return render(request, "home.html", context)

def room(request):
    return render(request, "room.html")