from django.db import models

# Create your models here.

class PaginaInicio(models.Model):
    mision=models.CharField(max_length=200, default='')
    vision=models.CharField(max_length=200, default='')
    quienesSomos=models.CharField(max_length=200, default='')

class Libros(models.Model):
    isb=models.CharField(max_length=20, default='')
    nombre=models.CharField(max_length=50, default='')
    imagen=models.ImageField(default='')
    disponible=models.BooleanField(default=False)

    def __str__(self):
        return 'Libros' + self.nombre, self.imagen, self.disponible

class Pedidos(models.Model):
    numeroOrden=models.IntegerField(default=0)
    nombre=models.CharField(max_length=20,default='')
    telefono=models.CharField(max_length=9, default='')
    correo=models.EmailField(default='')

class solicitudes(models.Model): # Solicitudes de contactos 
    nombre=models.CharField(max_length=20,default='')
    telefono=models.CharField(max_length=9, default='')
    correo=models.EmailField(default='')
    detalle=models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre, self.telefono, self.correo, self.detalle

class carritos(models.Model):
    isb=models.CharField(max_length=20, default='')
    nombre=models.CharField(max_length=50, default='')