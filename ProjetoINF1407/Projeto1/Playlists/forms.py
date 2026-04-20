from django import forms
from django.contrib.auth.models import User
from .models import Perfil
from Playlists.models import Musica

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'artista', 'album', 'genero', 'ano']


class AtualizarUsuarioForm(forms.ModelForm):
    foto_url = forms.URLField(
        required=False,
        label='Foto de perfil',
        widget=forms.URLInput(attrs={
            'placeholder': 'Cole aqui o link da sua foto',
            'class': 'form-control'
        })
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

        if self.user and hasattr(self.user, 'perfil'):
            self.fields['foto_url'].initial = self.user.perfil.foto_url

    def save(self, commit=True):
        user = super().save(commit=commit)

        if self.user:
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.foto_url = self.cleaned_data['foto_url']
            perfil.save()
        return user
