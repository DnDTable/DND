from django.shortcuts import render, redirect, get_object_or_404
from .models import Race, Bestiary, Item, Spell, Field
from django.core import serializers

def index(request):
    return redirect('wiki:race')

def race(request):
    races = serializers.serialize("python", Race.objects.all())

    context = {'races': races}
    return render(request, 'wiki/race.html', context)


def bestiary(request):
    bestiary = serializers.serialize("python", Bestiary.objects.all())

    context = {'bestiary': bestiary}
    return render(request, 'wiki/bestiary.html', context)


def items(request):
    items = serializers.serialize("python", Item.objects.all())

    context = {'items': items}
    return render(request, 'wiki/items.html', context)

def spells(request):
    spells = serializers.serialize("python", Spell.objects.all())

    context = {'spells': spells}
    return render(request, 'wiki/spells.html', context)

def classes(request):
    return render(request, 'wiki/classes.html')