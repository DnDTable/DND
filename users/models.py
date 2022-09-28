from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
