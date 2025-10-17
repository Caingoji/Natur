"""
URL configuration for Natur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from NaturApp import views
from NaturApp.views import infoUsuario
from NaturApp.views import base
from NaturApp.views import menu_pedidos
from NaturApp.views import lista_pedidos
from NaturApp.views import detalles_pedido
from NaturApp.views import pedido_empleado
from NaturApp.views import pedido_confirmado
from NaturApp.views import registrar_empleado
from NaturApp.views import registrar_cliente
from NaturApp.views import login
from NaturApp.views import menu_empleado
from NaturApp.views import menu_cliente
from NaturApp.views import logout
from NaturApp.views import eliminarPedido
from NaturApp.views import actualizarPedido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/',infoUsuario),
    path('',views.base, name="inicio"),
    path('login/', views.login, name='login'),
    path('registro_cliente/', views.registrar_cliente, name='registro_cliente'),
    path('menu_pedidos/', views.menu_pedidos, name='menu_pedidos'),
    path('pedido_confirmado/', views.pedido_confirmado, name='pedido_confirmado'),
    path('registro_empleado/', views.registrar_empleado, name='registro_empleado'),
    path('lista_pedidos/',lista_pedidos),
    path('pedido_empleado/',views.pedido_empleado, name='pedido_empleado'),
    path('eliminarPedido/<int:id>/', views.eliminarPedido, name='eliminarPedido'),
    path('actualizarPedido/<int:id>/', views.actualizarPedido, name='actualizarPedido'),
    path('detalles_pedido/', views.detalles_pedido, name='detalles_pedido'),
    path('menu_empleado/', views.menu_empleado, name='menu_empleado'),
    path('menu_cliente/', views.menu_cliente, name='menu_cliente'),
    path('logout/', views.logout, name='logout'),

]
