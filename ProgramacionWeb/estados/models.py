from django.db import models

from paises.models import Paises


# Create your models here.

class Estados(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.ForeignKey(Paises, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nombre} '
