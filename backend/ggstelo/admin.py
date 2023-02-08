from django.contrib import admin
from .models import Player
# Register your models here.


class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ('gamer_tag', 'elo', 'highest_elo',
                    'created_at', 'updated_at')
    search_fields = ('gamer_tag', 'slug')
    list_per_page = 50


admin.site.register(Player, PlayerModelAdmin)
