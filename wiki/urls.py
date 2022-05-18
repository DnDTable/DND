from django.urls import path
from . import views

app_name = 'wiki'
urlpatterns = [
    # Race
    path('race/', views.race, name='race'),
    # Beastiary
    path('bestiary/', views.bestiary, name='bestiary'),
]