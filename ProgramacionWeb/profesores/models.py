from django.db import models

from codigoPostal.models import CodigoPostal
from colonias.models import Colonias
from estados.models import Estados
from municipios.models import Municipios
from gradoEstudios.models import gradoEstudios


# Create your models here.

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellidoP = models.CharField(max_length=40)
    apellidoM = models.CharField(max_length=40)
    calle = models.CharField(max_length=60)
    numExt = models.CharField(max_length=5)
    numInt = models.CharField(max_length=5)
    colonia = models.ForeignKey(Colonias, on_delete=models.SET_NULL, null=True)
    cp = models.ForeignKey(CodigoPostal, on_delete=models.SET_NULL, null=True)
    municipio = models.ForeignKey(Municipios, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estados, on_delete=models.SET_NULL, null=True)
    gradoEstudios = models.ForeignKey(gradoEstudios, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f''
