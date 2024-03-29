from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # Home page
    path('chat/', views.index, name='index'),
    path('room/', views.room, name='room'),
    path('table/', views.table, name='table'),
]