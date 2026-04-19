from django import forms
from .models import Perfil
from Playlists.models import Musica

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'artista', 'album', 'genero', 'ano']
        


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto_url']
        labels = {
            'foto_url': 'URL da foto de perfil'
        }
        widgets = {
            'foto_url': forms.URLInput(attrs={
                'placeholder': 'Cole aqui o link da sua foto'
            })
        }