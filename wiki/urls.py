from django.urls import path
from . import views

app_name = 'wiki'
urlpatterns = [
    path('', views.index, name='index'),
    # Race
    path('race/', views.race, name='race'),
    # Beastiary
    path('bestiary/', views.bestiary, name='bestiary'),
    # Items
    path('items/', views.items, name='items'),
    # Spells
    path('spells/', views.spells, name='spells'),
    # Classes
    path('classes/', views.classes, name='classes'),
]