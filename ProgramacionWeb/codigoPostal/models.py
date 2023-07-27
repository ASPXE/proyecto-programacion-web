from django.db import models

from municipios.models import Municipios


# Create your models here.

class CodigoPostal(models.Model):
    cp = models.CharField(max_length=5)
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT)

    def __str__(self):
        return f'ID Codigo Postal: {self.id}, Codigo Postal: {self.cp}, Municipio: {self.municipio}'