from django.db import models
from django.contrib.auth.models import User

class Musica(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, help_text='Insira o título')
    artista = models.CharField(max_length=100, help_text='Insira o artista')
    album = models.CharField(max_length=100, blank=True, help_text='Insira o álbum') # blank = True ?
    genero = models.CharField(max_length=50, blank=True, help_text='Insira o gênero')
    ano = models.PositiveIntegerField(null=True, blank=True, help_text='Insira o ano de lançamento')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # ?

    def __str__(self):
        return f"{self.titulo} - {self.artista}"
    