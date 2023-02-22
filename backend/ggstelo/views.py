from decouple import config
from django.shortcuts import render
from rest_framework import generics, response, status, request as req, views
from .models import Player, Tournament
from .serializers import PlayerSerializer, TournamentSerializer

import pysmashgg

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


class TournamentDetailView(generics.GenericAPIView):
    serializer_class = TournamentSerializer

    def get(self, request, slug):
        query_set = Tournament.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)


class TournamentCreate(generics.CreateAPIView):

    def post(self, request):
        key = config('API_KEY')
        smash = pysmashgg.SmashGG(key, True)
        t_slug = request.data.get("url").split(
            "/tournament/")[1].split("/")[0]
        e_slug = request.data.get("url").split(
            "/event/")[1].split("/")[0]

        tournament = smash.tournament_show(t_slug)
        i = 1

        sets = []
        while (i > 0):

            results = smash.tournament_show_sets(t_slug, e_slug, i)
            sets.extend(results)

            if results == []:
                break
            i += 1
        print(len(sets))

        # serializer = TournamentSerializer(data=tournament)

       # if serializer.is_valid(raise_exception=True):
        #   tournament_saved = serializer.save()

        return response.Response({"success: Yay"})
