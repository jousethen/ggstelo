from decouple import config
from django.shortcuts import render
from rest_framework import generics, response, status, request as req, views
from .models import Player, Tournament, Match
from .serializers import PlayerSerializer, TournamentSerializer
from .libs import elo
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

        # Parse info we need from body
        t_slug = request.data.get("url").split(
            "/tournament/")[1].split("/")[0]
        e_slug = request.data.get("url").split(
            "/event/")[1].split("/")[0]

        # Get or Create Tournament
        tournament_data = smash.tournament_show(t_slug)
        tournament = Tournament.objects.get_or_create(
            slug=t_slug, name=tournament_data["name"])

        i = 1
        sets = []

        # Get All Sets (TODO move to helper)
        while (i > 0):
            results = smash.tournament_show_sets(t_slug, e_slug, i)
            sets.extend(results)

            if results == []:
                break
            i += 1

        # Iterate Sets
        for set in sets:
            # Skip if DQ
            if set["entrant1Score"] != -1 and set["entrant2Score"] != -1:
                # Get or Create players
                player1 = Player.objects.get_or_create(
                    id=set["entrant1Players"][0]["playerId"],
                    slug=set["entrant1Players"][0]["playerSlug"].split("/")[1],
                    gamer_tag=set["entrant1Players"][0]["playerTag"])
                player2 = Player.objects.get_or_create(
                    id=set["entrant2Players"][0]["playerId"],
                    slug=set["entrant2Players"][0]["playerSlug"].split("/")[1],
                    gamer_tag=set["entrant2Players"][0]["playerTag"])

                if (set["entrant1Score"] > set["entrant2Score"]):
                    calculated_elo = elo.calculate_elo(
                        player1[0], player2[0], 1)
                else:
                    calculated_elo = elo.calculate_elo(
                        player1[0], player2[0], 0)

                Match.objects.get_or_create(
                    id=set["id"],
                    player1=player1[0],
                    player1_score=set["entrant1Score"],
                    player2=player2[0],
                    player2_score=set["entrant2Score"],
                    player1_elo_change=calculated_elo[0] - player1[0].elo,
                    player2_elo_change=calculated_elo[1] - player2[0].elo,
                    tournament=tournament[0]
                )

        # serializer = TournamentSerializer(data=tournament)

       # if serializer.is_valid(raise_exception=True):
        #   tournament_saved = serializer.save()

        return response.Response({"success: Yay"})
