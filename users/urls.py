from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('', views.main, name='main'),
    # Register page
    path('register/', views.register, name='register'),
    # Login page
    path('login/', views.logon, name='login'),
    # Logout page
    path('logout/', LogoutView.as_view(), name='logout'),
    # Profile page
    path('proflie/', views.profile, name='proflie')
]