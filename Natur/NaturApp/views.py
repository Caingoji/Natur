from django.shortcuts import render

def infoUsuario(request):
    Data= { "Id":"123",
            "Nombre":"Clark Kent",
            "Direccion":"matamoro",
            "Telefono":"64862",
            "Correo":"superman@sm.gmail"}
    return render(request, 'templatesApp/Index.html',Data)

def inicio(request):
    return render(request, 'templatesApp/inicio.html')

def Mpedidos(request):
    return render(request,'templatesApp/menu_pedidos.html') 

def empleados(request):
    return render(request, 'templatesApp/empleado.html')