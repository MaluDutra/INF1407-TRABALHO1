from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from Playlists.models import Musica, Perfil
from Playlists.forms import MusicaForm, AtualizarUsuarioForm


def home(request):
    """
    Renderiza a página inicial do site.

    Essa view exibe a homepage pública do sistema, apresentando
    a proposta do site e os acessos principais.
    """
    return render(request, "playlists/home.html")


# CRUD de Músicas
@login_required
def listar_musicas(request):
    """
    Lista apenas as músicas cadastradas pelo usuário autenticado.

    O filtro por 'usuario=request.user' garante que cada usuário
    visualize somente sua própria playlist.
    """
    musicas = Musica.objects.filter(usuario=request.user)
    return render(request, 'playlists/listar_musicas.html', {'musicas': musicas})


@login_required
def adicionar_musica(request):
    """
    Permite ao usuário adicionar uma nova música à sua playlist.

    Se a requisição for POST, o formulário é validado e a música é salva.
    Antes do salvamento, o campo 'usuario' é preenchido com o usuário logado,
    garantindo a associação da música ao dono da playlist.
    """
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
    """
    Permite ao usuário editar uma música já cadastrada.

    A busca da música considera tanto o id quanto o usuário logado,
    impedindo que um usuário edite músicas de outra pessoa.
    """
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
    """
    Permite ao usuário remover uma música da sua playlist.

    A música só pode ser removida se pertencer ao usuário autenticado.
    No método GET, a página de confirmação é exibida.
    No método POST, a exclusão é efetivamente realizada.
    """
    musica = get_object_or_404(Musica, id=id, usuario=request.user)

    if request.method == 'POST':
        musica.delete()
        return redirect('listar_musicas')

    return render(request, 'playlists/confirmar_remocao.html', {'musica': musica})


# Controle de Usuário
def cadastro(request):
    """
    Realiza o cadastro de novos usuários no sistema.

    Utiliza o formulário padrão UserCreationForm do Django.
    Após o cadastro bem-sucedido, o usuário é autenticado automaticamente
    e redirecionado para a página de atualização de dados.
    """
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)  # autentica o usuário logo após o cadastro
            return redirect('atualizar_dados')
    else:
        formulario = UserCreationForm()

    contexto = {'form': formulario}
    return render(request, 'seguranca/cadastro.html', contexto)


def logout_usuario(request):
    """
    Exibe a página de logout.

    Esta view apresenta a tela de confirmação de saída da conta.
    O encerramento da sessão é realizado por outra rota específica
    configurada com LogoutView.
    """
    return render(request, 'seguranca/logout.html')


@login_required
def perfil(request):
    """
    Exibe a página de perfil do usuário autenticado.

    Caso o perfil ainda não exista, ele é criado automaticamente.
    A página mostra informações do usuário e dados complementares
    armazenados no modelo Perfil.
    """
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    contexto = {'perfil': perfil}
    return render(request, 'playlists/perfil.html', contexto)


@login_required
def atualizar_dados(request):
    """
    Permite atualizar os dados do usuário e do perfil.

    Essa view utiliza o formulário AtualizarUsuarioForm, que combina:
    - dados do modelo User, como username e email;
    - dados do modelo Perfil, como foto de perfil e música favorita.

    No POST, os dados são validados e salvos.
    No GET, o formulário é carregado com as informações atuais do usuário.
    """
    if request.method == 'POST':
        form = AtualizarUsuarioForm(request.POST, instance=request.user, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = AtualizarUsuarioForm(instance=request.user, user=request.user)

    contexto = {'form': form}
    return render(request, 'playlists/atualizar_dados.html', contexto)