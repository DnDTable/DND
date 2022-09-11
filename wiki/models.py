from django.db import models

class Bestiary(models.Model):
    """Бестиарий с существами и расами"""
    # Basic
    name = models.CharField(max_length=50)
    ideology = models.CharField(max_length=50)
    armor_class = models.CharField(max_length=50)
    health_points = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    move_speed = models.CharField(max_length=50)
    languages = models.CharField(max_length=100)
    danger = models.CharField(max_length=50)
    susceptibility = models.CharField(max_length=200)

    # characteristics
    strength = models.IntegerField(verbose_name='strength bonus', default=0)
    dexterity = models.IntegerField(verbose_name='dexterity bonus', default=0)
    constitution = models.IntegerField(verbose_name='constitution bonus', default=0)
    intelligence = models.IntegerField(verbose_name='intelligence bonus', default=0)
    wisdom = models.IntegerField(verbose_name='wisdom bonus', default=0)
    charisma = models.IntegerField(verbose_name='charisma bonus', default=0)

    # features
    feature_title = models.CharField(max_length=100)
    feature_description = models.TextField()

    # actions
    action_title = models.CharField(max_length=100)
    action_description = models.TextField()

    # about
    about_title = models.CharField(max_length=100, blank=True)
    about_description = models.TextField()

    def __str__(self):
        return self.name
