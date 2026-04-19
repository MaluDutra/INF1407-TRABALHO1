from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Musica(models.Model):
    """
    Modelo que representa uma música cadastrada no sistema.

    Cada música pertence a um usuário do sistema, permitindo que
    cada pessoa gerencie apenas suas próprias músicas.
    """

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        max_length=100,
        help_text='Insira o título'
    )
    artista = models.CharField(
        max_length=100,
        help_text='Insira o artista'
    )
    album = models.CharField(
        max_length=100,
        blank=True,
        help_text='Insira o álbum'
    )
    genero = models.CharField(
        max_length=50,
        blank=True,
        help_text='Insira o gênero'
    )
    ano = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Insira o ano de lançamento'
    )

    # Relaciona cada música ao usuário que a cadastrou.
    # Se o usuário for removido, suas músicas também serão excluídas.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna uma representação textual da música.
        """
        return f"{self.titulo} - {self.artista}"


class Perfil(models.Model):
    """
    Modelo que representa informações adicionais do usuário.

    Como o modelo User do Django não possui campo de foto de perfil,
    este modelo foi criado para armazenar dados complementares,
    como a URL da foto.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_url = models.URLField(blank=True, null=True)

    def __str__(self):
        """
        Retorna uma representação textual do perfil.
        """
        return f"Perfil de {self.user.username}"


@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    """
    Cria automaticamente um perfil para cada novo usuário cadastrado.

    Esse sinal é executado após o salvamento de um objeto User.
    Se o usuário tiver sido criado nesse momento, um Perfil
    correspondente é gerado automaticamente.
    """
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    """
    Garante que o perfil associado ao usuário também seja salvo.

    Esse sinal é executado após o salvamento de um objeto User.
    """
    perfil, _ = Perfil.objects.get_or_create(user=instance)
    perfil.save()