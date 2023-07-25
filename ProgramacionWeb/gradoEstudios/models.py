from django.db import models

# Create your models here.

class gradoEstudios(models.Model):
    grado = models.CharField(max_length=45)
