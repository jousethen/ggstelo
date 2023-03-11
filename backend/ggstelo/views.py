from requests import Response
from rest_framework import generics, response, status, request as req, views
from .models import Player, Tournament, Match
from .serializers import PlayerSerializer, TournamentSerializer
from .libs import elo, util
from decouple import config
import pysmashgg
from .paginators import CustomPagination

# Create your views here.


class PlayerListAPIView(generics.ListAPIView):
    serializer_class = PlayerSerializer
    pagination_class = CustomPagination
    queryset = Player.objects.all()

    @property
    def paginator(self):
        """The paginator instance associated with the view, or `None`."""
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """Return a single page of results, or `None` if pagination is disabled."""
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """Return a paginated style `Response` object for the given output data."""
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request):
        queryset = self.queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


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

        # Get All Sets (TODO move to helper)
        sets = util.get_sets(t_slug, e_slug)

        # Sort Sets by id (order which they happened)
        sets.sort(key=lambda x: x['id'], reverse=False)
        # Iterate Sets
        for set in sets:
            # Skip if DQ
            if set["entrant1Score"] != -1 and set["entrant2Score"] != -1:
                # Get or Create players
                player1 = Player.objects.get_or_create(
                    id=set["entrant1Players"][0]["playerId"])
                player1[0].slug = util.get_slug(
                    set["entrant1Players"][0]["playerSlug"])
                player1[0].gamer_tag = set["entrant1Players"][0]["playerTag"]
                player1[0].save()

                print(set["entrant2Players"][0]["playerSlug"],
                      set["entrant2Players"][0]["playerTag"])

                player2 = Player.objects.get_or_create(
                    id=set["entrant2Players"][0]["playerId"])
                player2[0].slug = util.get_slug(
                    set["entrant2Players"][0]["playerSlug"])
                player2[0].gamer_tag = set["entrant2Players"][0]["playerTag"]
                player2[0].save()

                match = Match.objects.get_or_create(id=set["id"])

                if match[1] == True:
                    # calculate elo
                    if (set["entrant1Score"] > set["entrant2Score"]):
                        calculated_elo = elo.calculate_elo(
                            player1[0], player2[0], 1)
                    else:
                        calculated_elo = elo.calculate_elo(
                            player1[0], player2[0], 0)
                    # Match Details
                    match[0].player1 = player1[0]
                    match[0].player1_score = set["entrant1Score"]
                    match[0].player2 = player2[0]
                    match[0].player2_score = set["entrant2Score"]
                    match[0].player1_elo_change = calculated_elo[0] - \
                        player1[0].elo
                    match[0].player2_elo_change = calculated_elo[1] - \
                        player2[0].elo
                    match[0].tournament = tournament[0]
                    match[0].save()

                    # Update Player Elos
                    player1[0].elo = calculated_elo[0]
                    player1[0].highest_elo = max(
                        calculated_elo[0], player1[0].highest_elo)
                    player1[0].save()

                    player2[0].elo = calculated_elo[1]
                    player2[0].highest_elo = max(
                        calculated_elo[1], player2[0].highest_elo)
                    player2[0].save()

        return response.Response({"success: Successfully imported tournament"})
