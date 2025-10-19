from django.db import models
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    nombre = models.CharField(max_length=25)
    numero = models.CharField(max_length=25)
    calle = models.CharField(max_length=50)
    cantidad_bidones = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=30,
        default='espera',
        choices=[
            ('espera', 'En espera'),
            ('camino', 'En camino'),
            ('entregado', 'Entregado')
        ]
    )

    def clean(self):
        if self.cantidad_bidones <= 0:
            raise ValidationError("La cantidad de bidones debe ser mayor que 0")

    def __str__(self):
        return f"{self.nombre}-{self.estado}"
    

class Pedido_Empleado(models.Model):
    nombre = models.CharField(max_length=50)  
    telefono = models.CharField(max_length=20)  
    direccion = models.CharField(max_length=100)  
    cantidad_bidones = models.IntegerField() 

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=30,
        default='espera',
        choices=[
            ('espera', 'En espera'),
            ('camino', 'En camino'),
            ('entregado', 'Entregado')
        ]
    )

    def __str__(self):
        return f"Pedido de {self.nombre} ({self.estado})"
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50, choices=[
        ('Repartidor', 'Repartidor'),
        ('Administrador', 'Administrador'),
        ('Atención al Cliente', 'Atención al Cliente'),
    ])

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"