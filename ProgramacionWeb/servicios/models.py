from django.db import models

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=45)
    costo = models.FloatField()