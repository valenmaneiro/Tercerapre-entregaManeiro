from django.db import models

# Create your models here.

class Futbolista(models.Model):
    nombreCompleto = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    equipo = models.CharField(max_length=60)
    dorsal = models.IntegerField()


class Entrenador(models.Model):
    nombreCompleto = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    equipo = models.CharField(max_length=60)

class Equipo(models.Model):
    nombre = models.CharField(max_length=60)
    pais = models.CharField(max_length=60)
    nroSocios = models.IntegerField()
    fechaFundacion = models.DateField()