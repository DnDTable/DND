from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Enable Auth url by default
    path('', include('django.contrib.auth.urls')),
    # Register page
    path('register/', views.register, name='register'),
]