from django.db import models

# Create your models here.
class Player(models.Model):
  id=models.CharField(max_length=50)
  slug=models.SlugField(max_length=50)
  gamer_tag=models.CharField(max_length=50)
  elo=models.PositiveIntegerField()
  highest_elo=models.PositiveIntegerField()
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  
  class Meta:
    ordering=('-gamer_tag',)
  
  def __str__(self):
    return self.gamer_tag

