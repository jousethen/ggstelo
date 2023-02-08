from django.urls import path
from .views import PlayerListAPIView, PlayerDetailAPIView

urlpatterns = [
    path('players', PlayerListAPIView.as_view(), name="players"),
    path('players/<str:slug>', PlayerDetailAPIView.as_view(), name="player")
]
