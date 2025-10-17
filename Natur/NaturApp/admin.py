from django.contrib import admin
from .models import Cliente, Pedido, Pedido_Empleado, Empleado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'telefono', 'direccion')
    search_fields = ('nombre', 'correo')
    list_filter = ('nombre',)
    ordering = ('id',)
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'correo', 'contrasena')
        }),
        ('Contacto', {
            'fields': ('direccion', 'telefono')
        }),
    )

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'numero', 'calle', 'cantidad_bidones', 'estado', 'fecha_creacion')
    list_filter = ('estado',)
    search_fields = ('nombre', 'numero')
    readonly_fields = ('fecha_creacion',)
    fieldsets = (
        ('Datos del Pedido', {
            'fields': ('nombre', 'numero', 'calle', 'cantidad_bidones')
        }),
        ('Estado y Fecha', {
            'fields': ('estado', 'fecha_creacion')
        }),
    )

@admin.register(Pedido_Empleado)
class PedidoEmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'direccion', 'cantidad_bidones', 'estado', 'fecha_creacion')
    list_filter = ('estado',)
    search_fields = ('nombre', 'telefono')
    readonly_fields = ('fecha_creacion',)
    fieldsets = (
        ('Datos del Pedido', {
            'fields': ('nombre', 'telefono', 'direccion', 'cantidad_bidones')
        }),
        ('Seguimiento', {
            'fields': ('estado', 'fecha_creacion')
        }),
    )

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'cargo')
    search_fields = ('nombre', 'correo', 'cargo')
    list_filter = ('cargo',)
    fieldsets = (
        ('Información del Empleado', {
            'fields': ('nombre', 'correo', 'contrasena')
        }),
        ('Detalles Laborales', {
            'fields': ('cargo',)
        }),
    )
