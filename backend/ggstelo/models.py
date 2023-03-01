
from django.db import models
from django.forms import ValidationError

# Create your models here.


class Player(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    slug = models.SlugField(max_length=50, unique=False)
    gamer_tag = models.CharField(max_length=50)
    elo = models.PositiveIntegerField(default=1000)
    highest_elo = models.PositiveIntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        ordering = ('elo',)

    def __str__(self):
        return self.gamer_tag

# Combination of Event and Tournament Model from Startgg


class Tournament(models.Model):
    slug = models.SlugField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

# Set from StartGG


class Match(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    player1 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='player1_match_set', null=True)
    player1_score = models.CharField(max_length=50)
    player2 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='player2_match_set', null=True)
    player2_score = models.CharField(max_length=50)
    player1_elo_change = models.IntegerField(default=0)
    player2_elo_change = models.IntegerField(default=0)
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "matches"

    def clean(self):
        if self.player1 == self.player2:
            raise ValidationError(('Player cannot play themselves'))

    def __str__(self):
        return self.id
