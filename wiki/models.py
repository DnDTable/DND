from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    specials = models.CharField(max_length=128)
    armor_class = models.IntegerField(default=0)
    move_speed = models.IntegerField(default=30)


class Characteristics(models.Model):
    strength = models.IntegerField()
    agility = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()


class Actions(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()


class Features(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()


class Description(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()


class RaceBestiary(models.Model):
    subclass_choice: list = [
        ('race', 'Игровая раса'),
        ('bestiary', 'Бестиарий')
    ]

    subclass = models.CharField(choices=subclass_choice, max_length=12)
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    characteristics = models.ForeignKey(Characteristics, on_delete=models.CASCADE)
    features = models.ForeignKey(Features, on_delete=models.CASCADE)
    actions = models.ForeignKey(Actions, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)


class Class(models.Model):
    title = models.CharField(max_length=128)


class Spell(models.Model):
    level = models.IntegerField()
    school = models.CharField(max_length=128)
    cast_time = models.CharField(max_length=128)
    distance = models.CharField(max_length=128)
    components = models.CharField(max_length=384)
    duration = models.CharField(max_length=128)
    classes = models.ManyToManyField(Class)


class Items(models.Model):
    field = models.ForeignKey(Description, on_delete=models.CASCADE)
