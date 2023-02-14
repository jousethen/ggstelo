from unicodedata import name
from django.contrib import admin
from .models import Player, Tournament, Match
# Register your models here.


class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ('gamer_tag', 'elo', 'highest_elo',
                    'created_at', 'updated_at')
    search_fields = ('gamer_tag', 'slug')
    list_per_page = 50


class TournamentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    list_per_page = 50


class MatchModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_score')
    search_fields = ('id', 'display_score')
    list_per_page = 50


admin.site.register(Player, PlayerModelAdmin)
admin.site.register(Tournament, TournamentModelAdmin)
admin.site.register(Match, MatchModelAdmin, name="Matches")
