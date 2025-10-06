from django.shortcuts import render,redirect

from .forms import PedidoForm
from .forms import pedidoFomrE

def infoUsuario(request):
    Data= { "Id":"123",
            "Nombre":"Clark Kent",
            "Direccion":"matamoro",
            "Telefono":"64862",
            "Correo":"superman@sm.gmail"}
    return render(request, 'templatesApp/Index.html',Data)

def inicio(request):
    return render(request, 'templatesApp/inicio.html')

def menu_pedidos(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido_confirmado')  
    else:
        form = PedidoForm()

    return render(request, 'templatesApp/menu_pedidos.html', {'form': form})


def pedido_confirmado(request):
    return render(request, 'templatesApp/confirmar_pedido.html')


def empleados(request):
    return render(request, 'templatesApp/empleado.html')

def pedido_empleado(request):
    if request.method == 'POST':
        form = pedidoFomrE(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')  
    else:
        form = PedidoForm()
    return render(request, 'templatesApp/pedido_empleado.html', {'form': form})

def detalles_pedido(request):
    return render(request, 'templatesApp/detalles_pedido.html')