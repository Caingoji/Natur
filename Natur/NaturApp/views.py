from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Pedido
from .forms import PedidoForm
from .forms import PedidoEmpleadoForm
from .forms import EmpleadoForm
from .forms import ClienteForm
from .models import Empleado,Cliente

def infoUsuario(request):
    Data= { "Id":"123",
            "Nombre":"Clark Kent",
            "Direccion":"matamoro",
            "Telefono":"64862",
            "Correo":"superman@sm.gmail"}
    return render(request, 'templatesApp/Index.html',Data)

def base(request):
    return render(request, 'templatesApp/base.html')

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente registrado correctamente.")
            return redirect('login_universal')
        else:
            messages.error(request, "Ocurrió un error. Revisa los datos ingresados.")
    else:
        form = ClienteForm()
    return render(request, 'templatesApp/registro_cliente.html', {'form': form})


def menu_pedidos(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pedido realizado con éxito.")
            return redirect('pedido_confirmado')
        else:
            messages.error(request, "Hubo un error con tu pedido. Inténtalo nuevamente.")
    else:
        form = PedidoForm()
    return render(request, 'templatesApp/menu_pedidos.html', {'form': form})


def pedido_confirmado(request):
    return render(request, 'templatesApp/confirmar_pedido.html')


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'templatesApp/lista_pedidos.html', {'pedidos': pedidos})

def eliminarPedido(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    return redirect('/lista_pedidos')

def actualizarPedido(request, id):
    pedido = Pedido.objects.get(id=id)
    form = PedidoForm(instance=pedido)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('/lista_pedidos')

    data = {'form': form}
    return render(request, 'templatesApp/editar_pedido_empleado.html', data)



def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = EmpleadoForm()
    return render(request, 'templatesApp/registro_empleado.html', {'form': form})


def pedido_empleado(request):
    if request.method == 'POST':
        form = pedido_empleado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')  
    else:
        form = PedidoForm()
    return render(request, 'templatesApp/detalles_pedido.html', {'pedido': PedidoEmpleadoForm})



def detalles_pedido(request):
    pedido = Pedido.objects.last() 
    return render(request, 'templatesApp/detalles_pedido.html', {'pedido': pedido})


def login(request):
    error = None

    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')

        empleado = Empleado.objects.filter(correo=correo, contrasena=contrasena).first()
        if empleado:
            request.session['usuario_id'] = empleado.id
            request.session['usuario_tipo'] = 'empleado'
            return redirect('menu_empleado')

        cliente = Cliente.objects.filter(correo=correo, contrasena=contrasena).first()
        if cliente:
            request.session['usuario_id'] = cliente.id
            request.session['usuario_tipo'] = 'cliente'
            return redirect('menu_cliente')

        error = "Correo o contraseña incorrectos"

    return render(request, 'templatesApp/login_universal.html', {'error': error})

def menu_empleado(request):
    if request.session.get('usuario_tipo') != 'empleado':
        return redirect('login')
    return render(request, 'templatesApp/menu_empleado.html')


def menu_cliente(request):
    if request.session.get('usuario_tipo') != 'cliente':
        return redirect('login')
    return render(request, 'templatesApp/menu_cliente.html')

def logout(request):
    request.session.flush()
    return redirect('login')
