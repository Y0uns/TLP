from django.db import models

class Carrera(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()

    def __str__(self) :
        return self.codigo
    
class Docente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self) :
        return self.nombre + " "+ self.apellido + " " + self.email  