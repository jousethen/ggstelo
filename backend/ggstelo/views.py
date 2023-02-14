from django.shortcuts import render
from rest_framework import generics, response, status, request
from .models import Player, Tournament
from .serializers import PlayerSerializer, TournamentSerializer
# Create your views here.


class PlayerListAPIView(generics.ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all()


class PlayerDetailAPIView(generics.GenericAPIView):
    serializer_class = PlayerSerializer

    def get(self, request, slug):
        print(request)
        query_set = Player.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)

# Tournament Views


class TournamentListAPIView(generics.ListAPIView):
    serializer_class = TournamentSerializer

    def get_queryset(self):
        return Tournament.objects.all()


class TournamentDetailAPIView(generics.GenericAPIView):
    serializer_class = TournamentSerializer

    def get(self, request, slug):
        print(request.method)
        query_set = Tournament.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)
