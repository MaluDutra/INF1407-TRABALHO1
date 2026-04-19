from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    
    

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()