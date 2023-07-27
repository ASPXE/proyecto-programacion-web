from django.db import models

# Create your models here.

class Paises(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return f'ID Paises: {self.id}, Nombre: {self.nombre}'