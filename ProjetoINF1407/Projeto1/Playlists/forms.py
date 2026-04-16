from django import forms
from Playlists.models import Musica

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'artista', 'album', 'genero', 'ano']
        