from Playlists import views
from django.urls import path
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home, name='homepage'),
    path('listar', views.listar_musicas, name='listar_musicas'),
    path('adicionar/', views.adicionar_musica, name='adicionar_musica'),
    path('editar/<int:id>/', views.editar_musica, name='editar_musica'),
    path('remover/<int:id>/', views.remover_musica, name='remover_musica'),
    path('perfil/', views.perfil, name='perfil'),
]
