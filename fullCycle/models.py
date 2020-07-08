from django.db import models

# Create your models here.
class Aula(models.Model):

    titulo = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    data = models.CharField(
        max_length=18,
        null=False,
        blank=False
    )

    apresentador = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    objetos = models.Manager()
