from django.db import models



# mudanças da érica
from django.contrib.auth.models import User

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True)
    genero = models.CharField(max_length=50, blank=True)
    ano = models.PositiveIntegerField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"