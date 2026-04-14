# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Alô mundo!')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Musica
from .forms import MusicaForm

@login_required
def listar_musicas(request):
    musicas = Musica.objects.filter(usuario=request.user)
    return render(request, 'Playlists/listar_musicas.html', {'musicas': musicas})

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

    return render(request, 'Playlists/form_musica.html', {'form': form, 'acao': 'Adicionar'})

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

    return render(request, 'Playlists/form_musica.html', {'form': form, 'acao': 'Editar'})

@login_required
def remover_musica(request, id):
    musica = get_object_or_404(Musica, id=id, usuario=request.user)

    if request.method == 'POST':
        musica.delete()
        return redirect('listar_musicas')

    return render(request, 'Playlists/confirmar_remocao.html', {'musica': musica})