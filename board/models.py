from django.db import models
from django.contrib.auth.models import User
from users.models import Player


class Board(models.Model):
    board_name = models.CharField(max_length=100)
    game_master = models.ForeignKey(Player, on_delete=models.CASCADE)


