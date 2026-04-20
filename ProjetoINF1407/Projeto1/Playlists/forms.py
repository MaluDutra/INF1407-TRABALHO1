from django import forms
from django.contrib.auth.models import User
from .models import Perfil
from Playlists.models import Musica

class MusicaForm(forms.ModelForm):
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
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user is not None:
            self.fields['musica_favorita'].queryset = Musica.objects.filter(usuario=self.user)

            if hasattr(self.user, 'perfil'):
                self.fields['foto_url'].initial = self.user.perfil.foto_url
                self.fields['musica_favorita'].initial = self.user.perfil.musica_favorita

    def save(self, commit=True):
        user = super().save(commit=commit)

        if self.user:
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.foto_url = self.cleaned_data['foto_url']
            perfil.musica_favorita = self.cleaned_data['musica_favorita']
            perfil.save()
        return user
