import uuid
from django.db import models
from django.contrib.auth.models import User


class Primary(models.Model):
    class_and_level = models.CharField(max_length=128)
    race = models.CharField(max_length=64)
    background = models.CharField(max_length=128)
    alignment = models.CharField(max_length=128)
    player_name = models.CharField(max_length=64)
    experience_points = models.IntegerField()


class Secondary(models.Model):
    inspiration = models.IntegerField()
    proficiency_bonus = models.IntegerField()
    armor = models.IntegerField()
    initiative = models.IntegerField()
    speed = models.IntegerField()


class Characteristics(models.Model):
    strength = models.IntegerField()
    agility = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()


class Skills(models.Model):
    acrobatics = models.IntegerField()
    animal_handling = models.IntegerField()
    arcana = models.IntegerField()
    athletics = models.IntegerField()
    deception = models.IntegerField()
    history = models.IntegerField()
    intimidation = models.IntegerField()
    investigation = models.IntegerField()
    medicine = models.IntegerField()
    nature = models.IntegerField()
    perception = models.IntegerField()
    performance = models.IntegerField()
    persuasion = models.IntegerField()
    religion = models.IntegerField()
    sleight_of_hand = models.IntegerField()
    stealth = models.IntegerField()
    survival = models.IntegerField()


class Bio(models.Model):
    personality_trait = models.TextField()
    ideals = models.TextField()
    ties = models.TextField()
    flaws = models.TextField()


class SpellAndAttack(models.Model):
    title = models.CharField(max_length=128)
    bonus = models.IntegerField()
    damage_and_type = models.CharField(max_length=256)


class Health(models.Model):
    current_hp = models.IntegerField()
    temporary_hp = models.IntegerField()
    hit_dice = models.IntegerField()
    # TODO: DEATH SAVES???


class Miscellaneous(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()


class Exterior(models.Model):
    age = models.CharField(max_length=64)
    eyes = models.CharField(max_length=64)
    skin = models.CharField(max_length=64)
    hair = models.CharField(max_length=64)
    growth = models.CharField(max_length=64)
    weight = models.CharField(max_length=64)
    description = models.TextField()


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
