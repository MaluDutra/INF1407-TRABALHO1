from Playlists import views
from django.contrib import admin
from django.urls import path, include
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', views.home, name='homepage'),
    path('listar', views.listar_musicas, name='listar_musicas'),
    path('adicionar/', views.adicionar_musica, name='adicionar_musica'),
    path('editar/<int:id>/', views.editar_musica, name='editar_musica'),
    path('remover/<int:id>/', views.remover_musica, name='remover_musica'),
    path('perfil/', views.perfil, name='perfil'),
    path(
    'seguranca/password_change/',
    PasswordChangeView.as_view(
        template_name='seguranca/password_change_form.html',
        success_url=reverse_lazy('sec-password_change_done'),
    ),
    name='sec-password_change'
),

path(
    'seguranca/password_change_done/',
    PasswordChangeDoneView.as_view(
        template_name='seguranca/password_change_done.html',
    ),
    name='sec-password_change_done'
),


]
