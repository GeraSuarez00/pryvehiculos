from django import forms
from apps.ventas.models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
 
        fields = [
            'fecha',
            'ValorTotal',
            'tipoPago',
            'user',
            # 'vehiculo',
        ]
        labels = {
            'fecha':'Ingrese la fecha',
            'ValorTotal':'Ingrese el valor total',
            'tipoPago': 'Ingrese el tipo de pago',
            'user': 'Elija el usuario',
            # 'vehiculo': 'Elija el vehiculo',
        }

        widgets ={
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'ValorTotal': forms.TextInput(attrs={'class': 'form-control'}),
            # 'tipoPago': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoPago': forms.Select(attrs={'class': 'form-control'}, choices='tipoPago_choices'),
            'user': forms.Select(attrs={'class': 'form-control'}),
            # 'vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }