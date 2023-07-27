from django.db import models

from codigoPostal.models import CodigoPostal


# Create your models here.

class Colonias(models.Model):
    nombre = models.CharField(max_length=45)
    codigoPostal = models.ForeignKey(CodigoPostal, on_delete=models.PROTECT)

    def __str__(self):
        return f'ID Colonia: {self.id}, Nombre: {self.nombre}, Codigo Postal: {self.codigoPostal}'
