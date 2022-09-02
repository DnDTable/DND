from django.urls import path, include


from . import views

app_name = 'users'
urlpatterns = [
    # Main page that user sees when connects
    path('', views.main, name='main'),
    # Register page
    path('register/', views.register, name='register'),
    # Login page
    path('login/', views.login, name='login'), # заглушка, не работает
]