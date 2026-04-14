from django.urls import path
from Playlists import views

urlpatterns = [
    path('', views.home),
] 
