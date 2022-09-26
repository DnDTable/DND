from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required()
def index(request):
    """Home page"""
    return render(request, 'board/chat.html')

@login_required()
def table(request):
    return render(request, 'board/server-client.html')