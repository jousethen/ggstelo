from rest_framework import serializers
from .models import Player, Tournament


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ["id", "slug", "gamer_tag", "elo", "highest_elo",
                  "player1_match_set", "player2_match_set"]


class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ["name", "slug", "match_set"]
