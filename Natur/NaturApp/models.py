from django.db import models

class Pedido(models.Model):
    nombre= models.CharField(max_length=25)
    numero=models.CharField(max_length=25)
    calle=models.CharField(max_length=50)
    cantidad_bidones=models.IntegerField()

    fecha_creacion=models.DateTimeField(auto_now_add=True)
    estado=models.CharField(
        max_length=30,
        default='espera',
        choices=[
            ('en espera','en espera'),
            ('en camino','en camino'),
            ('entregado', 'entregado')
        ]
    )

    def __str__(self):
        return f"{self.nombre}-{self.estado}"


class Pedido_Empleado(models.Model):
    nombre = models.CharField(max_length=50)  
    telefono = models.CharField(max_length=20)  
    direccion = models.CharField(max_length=100)  
    cantidad_bidones = models.IntegerField() 

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('espera', 'En espera'),
            ('camino', 'En camino'),
            ('entregado', 'Entregado')
        ],
        default='espera'
    )

    def __str__(self):
        return f"Pedido de {self.nombre} ({self.estado})"