from django.db import models

from municipios.models import Municipios


# Create your models here.

class CodigoPostal(models.Model):
    cp = models.CharField(max_length=5)
    municipio = models.ForeignKey(Municipios, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.cp}'