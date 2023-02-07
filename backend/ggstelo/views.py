from django.shortcuts import render
from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer

# Create your views here.
class PlayerListAPIView(generics.ListAPIView):
  serializer_class=PlayerSerializer
  
  def get_queryset(self):
      return Player.objects.all()
  