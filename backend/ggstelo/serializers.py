from rest_framework import serializers
from .models import Player, Tournament, CustomUserModel
from django.conf import settings

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ["id", "slug", "gamer_tag", "elo", "highest_elo",
                  "player1_match_set", "player2_match_set"]


class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ["name", "slug", "match_set"]

class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = [
            "userId",
            "username",
            "email", 
            "password",
        ]
    def create(self, validated_data):
        user = CustomUserModel.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"]
        )
        
        return user