from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=60) 
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    profesion = models.CharField(max_length=60)

class Entregable(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField()    