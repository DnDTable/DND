from django.contrib import admin
from .models import Bestiary, Item, Spell, Race, Field

admin.site.register(Race)
admin.site.register(Bestiary)
admin.site.register(Item)
admin.site.register(Spell)
admin.site.register(Field)
