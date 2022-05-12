from django.urls import path
from apps.vehiculos.views import listVehiculos, vehiculoCreate, vehiculoEdit, vehiculoEliminar

app_name='vehiculos' #este el nombre que puse en namespace del archivo urls.py de pryvehiculos
urlpatterns = [
    path('', listVehiculos, name='listVehiculos'), # cuando digan vehiculo/ ejecuta el método listVehiculos
    path('nuevo/', vehiculoCreate, name='vehiculoCreate'), 
    path('actualizar/<int:id_vehiculo>/', vehiculoEdit, name='vehiculoEdit'), #el del medio es un método que se debe importar en vista, y el ultimo es el nombre que le doy para llamarlo desde un menú
    path('eliminar/<int:id_vehiculo>/', vehiculoEliminar, name='vehiculoEliminar'), 
    ]
