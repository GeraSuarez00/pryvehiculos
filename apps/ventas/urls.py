from django.urls import path
from apps.ventas.views import *
app_name='ventas' #este el nombre que puse en namespace del archivo urls.py de pryvehiculos
urlpatterns = [
    path('', listVentas, name='listVentas'), # cuando digan vehiculo/ ejecuta el método listVehiculos
    path('nuevo/', ventaCreate, name='ventaCreate'), 
    path('actualizar/<int:id_venta>/', ventaEdit, name='ventaEdit'), #el del medio es un método que se debe importar en vista, y el ultimo es el nombre que le doy para llamarlo desde un menú
    path('eliminar/<int:id_venta>/', ventaEliminar, name='ventaEliminar'), 
    
    #VehiculoVenta
    path('VehiculoVenta/', listVehiculoVentas, name='listVehiculoVentas'),
    path('nuevo_vv/', vehiculoVentasCreate, name='vehiculoVentasCreate'), 
    path('actualizar_vv/<int:id_vehiculoVenta>/', vehiculoVentasEdit, name='vehiculoVentasEdit'), 
    path('eliminar_vv/<int:id_vehiculoVenta>/', vehiculoVentasEliminar, name='vehiculoVentasEliminar'), 

    #Usuarios
    path('Usuarios/', listUsuarios, name='listUsuarios'),
    path('nuevo_u/', usuariosCreate, name='usuariosCreate'), 
    path('actualizar_u/<int:id_usuario>/', usuariosEdit, name='usuariosEdit'), 
    path('eliminar_u/<int:id_usuario>/', usuariosEliminar, name='usuariosEliminar'), 
   
    ]