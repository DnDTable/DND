from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Room, Board

@login_required()
def index(request):
    """Home page"""
    return render(request, 'board/chat.html')

@login_required()
def table(request, slug):
    room = Room.objects.get(slug=slug)
    players = Board.objects.get(1)
    return render(request, 'board/server-client.html', {'room': room, 'players': players})

@login_required()
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'board/rooms.html', {'rooms': rooms})

