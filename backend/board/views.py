from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Home page"""
    return render(request, 'board/chat.html')
