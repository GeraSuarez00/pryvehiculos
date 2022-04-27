from django.contrib import admin
from apps.vehiculos.models import Vehiculo, TipoVehiculo,Marca
# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo','color','placa','motor','marca','tipovehiculo')#muestra los campos que indico y su contenido
    ordering = ('modelo','color','placa','motor','marca','tipovehiculo') #ordena los campos en el orden q indica
    search_fields = ['modelo','marca__nombre'] #campos por los que quiero que se busque, cuando es llave foránea pongo dos guiones como en marca__nombre
    list_filter= ('modelo','marca__nombre','tipovehiculo__nombre') #se coloca al lado derecho lo que se quiere filtrar
admin.site.register(TipoVehiculo)
admin.site.register(Marca)
admin.site.register(Vehiculo,VehiculoAdmin)