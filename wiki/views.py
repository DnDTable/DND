from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


@login_required()
def races(request):
    return render(request, 'wiki/races.html')


@login_required()
def bestiary(request):
    return render(request, 'wiki/bestiary.html')


@login_required()
def classes(request):
    return render(request, 'wiki/classes.html')


@login_required()
def items(request):
    return render(request, 'wiki/items.html')


@login_required()
def spells(request):
    return render(request, 'wiki/spells.html')


@login_required()
def content(request):
    return render(request, 'wiki/content.html')
