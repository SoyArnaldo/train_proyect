from django.db import models
from django.utils.translation import gettext_lazy as _
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    titulo= models.CharField(max_length=120, default='Zona del cuerpo a entrenar')
    video = EmbedVideoField()  # same like models.URLField()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario = models.CharField(max_length=200, default="Cuentanos que te parece la experiencia del usuario")
