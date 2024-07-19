from django.db import models

# Create your models here.
class Empresa(models.Model):
    rut_empresa = models.CharField(max_length=20, primary_key=True)
    nombre_emp = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_emp

class Comuna(models.Model):
    id_comuna = models.CharField(max_length=30, primary_key=True)
    nombre_comuna = models.CharField(max_length=20)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_comuna

class Region(models.Model):
    id_region = models.CharField(max_length=20, primary_key=True)
    nombre_region = models.CharField(max_length=20)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_region

class Pagina(models.Model):
    id_pagina = models.CharField(max_length=30, primary_key=True)
    nombre_pagina = models.CharField(max_length=20)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_pagina

class Carrito(models.Model):
    id_carrito = models.CharField(max_length=30, primary_key=True)
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_carrito

class Producto(models.Model):
    id_producto = models.CharField(max_length=20, primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre_producto

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=20, null=True, blank=True)
    apellido = models.CharField(max_length=20, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_usuario
