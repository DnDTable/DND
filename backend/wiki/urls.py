from django.urls import path
from . import views

app_name = 'wiki'
urlpatterns = [
    # Race
    path('races/', views.races, name='races'),
    # Beastiary
    path('bestiary/', views.bestiary, name='bestiary'),
    # Spells
    path('spells/', views.spells, name='spells'),
    # Items
    path('items/', views.items, name='items'),
    # Classes
    path('classes/', views.classes, name='classes'),
    # # Contents
    path('', views.content, name='content')

]
