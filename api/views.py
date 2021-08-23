from django.shortcuts import redirect, render
from django.http import HttpResponse

from rest_framework import generics

from .models import Room

from .serializers import RoomSerializer



def main(request):
    return HttpResponse("<h1>Hello</h1>")

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

