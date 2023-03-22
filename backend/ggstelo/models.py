
from email.message import EmailMessage
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from uuid import uuid4
# Create your models here.

class CustomUserModelManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
            Creates a custom user with given fields
        """

        user = self.model(
            username = username, 
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser (self, username, email, password):
        user = self.create_user(
            username, 
            email, 
            password = password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user
    
class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    userId = models.CharField(max_length = 16, default = uuid4, primary_key = True, editable = False)
    username = models.CharField(max_length= 16, unique = True, null = False, blank = False)
    email = models.EmailField(max_length = 100, unique = True, null = False, blank = False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    active = models.BooleanField(default = True)

    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    created_on = models.DateTimeField(auto_now_add= True, blank = True, null = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CustomUserModelManager()

    class Meta:
        verbose_name = "Custom User"
class Player(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    slug = models.SlugField(max_length=50, unique=False)
    gamer_tag = models.CharField(max_length=50)
    elo = models.PositiveIntegerField(default=1000)
    highest_elo = models.PositiveIntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-elo',)

    def __str__(self):
        return self.gamer_tag

# Combination of Event and Tournament Model from Startgg


class Tournament(models.Model):
    slug = models.SlugField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

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
