from django.shortcuts import render


def races(request):
    return render(request, 'wiki/races.html')


def bestiary(request):
    return render(request, 'wiki/bestiary.html')


def classes(request):
    return render(request, 'wiki/classes.html')


def items(request):
    return render(request, 'wiki/items.html')


def spells(request):
    return render(request, 'wiki/spells.html')


def content(request):
    return render(request, 'wiki/content.html')