from django import forms
from apps.vehiculos.models import TipoVehiculo

class TipoVehiculosForm(forms.ModelForm):
    class Meta:
        model = TipoVehiculo
    
        fields = [
            'nombre',
        ]
 
        labels = {
            'nombre': 'Ingrese el nombre',
        }

        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
        }
