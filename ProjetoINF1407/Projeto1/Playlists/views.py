from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from Playlists.models import Musica
from Playlists.forms import MusicaForm
from .models import Perfil
from .forms import PerfilForm

def home(request):
    return render(request, "playlists/home.html")

# CRUD de adicionar músicas
@login_required
def listar_musicas(request):
    musicas = Musica.objects.filter(usuario=request.user)
    return render(request, 'playlists/listar_musicas.html', {'musicas': musicas})

@login_required
def adicionar_musica(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.usuario = request.user
            musica.save()
            return redirect('listar_musicas')
    else:
        form = MusicaForm()

    return render(request, 'playlists/form_musica.html', {'form': form, 'acao': 'Adicionar'})

@login_required
def editar_musica(request, id):
    musica = get_object_or_404(Musica, id=id, usuario=request.user)

    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('listar_musicas')
    else:
        form = MusicaForm(instance=musica)

    return render(request, 'playlists/form_musica.html', {'form': form, 'acao': 'Editar'})

@login_required
def remover_musica(request, id):
    musica = get_object_or_404(Musica, id=id, usuario=request.user)

    if request.method == 'POST':
        musica.delete()
        return redirect('listar_musicas')

    return render(request, 'playlists/confirmar_remocao.html', {'musica': musica})

# Controle de Usuário
def cadastro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario) # Loga o usuário após o cadastro
            return redirect('homepage')
    else:
        formulario = UserCreationForm()
    contexto = {'form': formulario }
    return render(request, 'playlists/cadastro.html', contexto)

def logout_usuario(request):
    # logout(request)
    # return render(request, 'playlists/home.html')
    return render(request, 'playlists/logout.html')


@login_required
def perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)

    contexto = {
        'perfil': perfil,
        'form': form,
    }
    return render(request, 'seguranca/perfil.html', contexto)