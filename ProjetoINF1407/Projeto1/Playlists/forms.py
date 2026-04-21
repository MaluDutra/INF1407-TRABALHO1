from django import forms
from django.contrib.auth.models import User
from .models import Perfil
from Playlists.models import Musica


class MusicaForm(forms.ModelForm):
    """
    Formulário baseado no modelo Musica.

    Esse formulário é utilizado para cadastrar e editar músicas da playlist
    do usuário. Além dos campos textuais básicos da música, ele também permite
    informar:
    - a URL da imagem/capa da música;
    - o link para ouvir a música.
    """

    class Meta:
        model = Musica
        fields = ['titulo', 'artista', 'album', 'genero', 'ano', 'imagem_url', 'link_musica']
        labels = {
            'imagem_url': 'URL da capa da música',
            'link_musica': 'Link para ouvir a música'
        }
        widgets = {
            'imagem_url': forms.URLInput(attrs={
                'placeholder': 'Cole aqui o link da capa da música',
                'class': 'form-control'
            }),
            'link_musica': forms.URLInput(attrs={
                'placeholder': 'Cole aqui o link para ouvir a música',
                'class': 'form-control'
            })
        }


class AtualizarUsuarioForm(forms.ModelForm):
    """
    Formulário para atualização dos dados do usuário e do perfil.

    Esse formulário edita simultaneamente:
    - dados do modelo User (nome de usuário e e-mail);
    - dados do modelo Perfil (foto de perfil e música favorita).

    Como o modelo User do Django não possui diretamente campos como
    foto_url e musica_favorita, esses campos foram adicionados
    manualmente ao formulário e tratados no método save().
    """

    foto_url = forms.URLField(
        required=False,
        label='Foto de perfil',
        widget=forms.URLInput(attrs={
            'placeholder': 'Cole aqui o link da sua foto',
            'class': 'form-control'
        })
    )

    musica_favorita = forms.ModelChoiceField(
        queryset=Musica.objects.none(),
        required=False,
        label='Música favorita',
        empty_label='Selecione sua música favorita',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Nome de usuário',
            'email': 'E-mail'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Inicializa o formulário.

        Recebe opcionalmente o usuário logado através do parâmetro 'user'
        para permitir duas customizações importantes:

        1. Filtrar o campo 'musica_favorita', mostrando apenas músicas
           pertencentes ao usuário atual;
        2. Preencher automaticamente os campos extras do formulário
           com os dados já salvos no perfil do usuário.
        """
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user is not None:
            # Limita as opções de música favorita às músicas cadastradas
            # pelo próprio usuário.
            self.fields['musica_favorita'].queryset = Musica.objects.filter(usuario=self.user)

            # Se o usuário já possui perfil criado, carrega os dados atuais
            # para exibição inicial no formulário.
            if hasattr(self.user, 'perfil'):
                self.fields['foto_url'].initial = self.user.perfil.foto_url
                self.fields['musica_favorita'].initial = self.user.perfil.musica_favorita

    def save(self, commit=True):
        """
        Salva as alterações no usuário e no perfil.

        Primeiro, salva os dados do modelo User através do método save()
        herdado do ModelForm.

        Em seguida:
        - busca ou cria o Perfil associado ao usuário;
        - atualiza a foto de perfil;
        - atualiza a música favorita;
        - salva o perfil.

        Retorna o objeto User atualizado.
        """
        user = super().save(commit=commit)

        if self.user:
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.foto_url = self.cleaned_data['foto_url']
            perfil.musica_favorita = self.cleaned_data['musica_favorita']
            perfil.save()

        return user