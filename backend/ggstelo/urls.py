from django.urls import path
from .views import *

urlpatterns = [
    path('players', PlayerListAPIView.as_view(), name="players"),
    path('players/<str:slug>', PlayerDetailAPIView.as_view(), name="player"),
    path('tournaments', TournamentListAPIView.as_view(), name="tournaments"),
    path('tournaments/<str:slug>',
         TournamentDetailAPIView.as_view(), name="tournament")
]
