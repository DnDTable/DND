from django.db import models


class Field(models.Model):
    title = models.CharField(max_length=120)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Bestiary(models.Model):
    """Бестиарий с существами"""
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
    feature = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='bestiary_features', default='')

    # actions
    action = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='bestiary_actions', default='')

    # about
    about = models.TextField()

    class Meta:
        verbose_name_plural = 'Bestiaries'

    def __str__(self):
        return self.name


class Race(models.Model):
    """Расы"""
    # Basic
    name = models.CharField(max_length=50)
    ideology = models.CharField(max_length=50)
    armor_class = models.CharField(max_length=50)
    health_points = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    move_speed = models.CharField(max_length=50)
    languages = models.CharField(max_length=100)
    danger = models.CharField(max_length=50, default='')
    susceptibility = models.CharField(max_length=200)

    # characteristics
    strength = models.IntegerField(verbose_name='strength bonus', default=0)
    dexterity = models.IntegerField(verbose_name='dexterity bonus', default=0)
    constitution = models.IntegerField(verbose_name='constitution bonus', default=0)
    intelligence = models.IntegerField(verbose_name='intelligence bonus', default=0)
    wisdom = models.IntegerField(verbose_name='wisdom bonus', default=0)
    charisma = models.IntegerField(verbose_name='charisma bonus', default=0)

    # features
    feature = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='race_features', default='')

    # actions
    action = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='race_actions', default='')

    # about
    about = models.TextField()

    class Meta:
        verbose_name_plural = 'Races'

    def __str__(self):
        return self.name


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.item_name


class Spell(models.Model):
    # basic
    title = models.CharField(max_length=100)
    school = models.CharField(max_length=50)
    cast_time = models.CharField(max_length=50)
    cast_distance = models.CharField(max_length=50)
    component = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    classes = models.CharField(max_length=100)

    # about
    about = models.TextField()

    class Meta:
        verbose_name_plural = 'Spells'

    def __str__(self):
        return self.title
