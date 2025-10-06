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
from NaturApp.views import inicio
from NaturApp.views import menu_pedidos
from NaturApp.views import empleados
from NaturApp.views import detalles_pedido
from NaturApp.views import pedido_empleado
from NaturApp.views import pedido_confirmado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/',infoUsuario),
    path('inicio/',inicio),
    path('menu_pedidos/', views.menu_pedidos, name='menu_pedidos'),
    path('pedido_confirmado/', views.pedido_confirmado, name='pedido_confirmado'),
    path('empleado/',empleados),
    path('pedido_empleado/',views.pedido_empleado, name='pedido_empleado'),
    path('pedido/', detalles_pedido)
]
