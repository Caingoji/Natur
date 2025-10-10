from django import forms
from .models import Pedido
from .models import Pedido_Empleado
from .models import Empleado
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'contrasena', 'direccion', 'telefono']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model=Pedido
        fields=('nombre','numero','calle','cantidad_bidones')


class PedidoEmpleadoForm(forms.ModelForm):
      class Meta:
        model = Pedido_Empleado
        fields = ['nombre', 'telefono', 'direccion', 'cantidad_bidones']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'correo', 'contrasena', 'cargo']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
