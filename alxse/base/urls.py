from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=("home.html")),
    path('room/', views.room, name="room.html")
]
