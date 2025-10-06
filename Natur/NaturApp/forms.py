from django import forms
from .models import Pedido
from .models import Pedido_Empleado

class PedidoForm(forms.ModelForm):
    class Meta:
        model=Pedido
        fields=('nombre','numero','calle','cantidad_bidones')


class pedidoFomrE(forms.ModelForm):
      class Meta:
        model = Pedido_Empleado
        fields = ['nombre', 'telefono', 'direccion', 'cantidad_bidones']