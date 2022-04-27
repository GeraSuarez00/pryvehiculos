from django.contrib import admin
from apps.ventas.models import Venta, VehiculoVenta

class MembershipInline(admin.TabularInline):
    model = VehiculoVenta
    extra = 1 #indico la cantidad de campos que quiero para insertar en el formulario, si yo comento esta línea me pone 3 campos por defecto

class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha','ValorTotal','tipoPago','user')#muestra los campos que indico y su contenido
    ordering = ('fecha','user') #ordena los campos en el orden q indica
    search_fields = ('fecha',) #campos por los que quiero que se busque, cuando es llave foránea pongo dos guiones como en marca__nombre
    list_filter= ('fecha','ValorTotal','tipoPago','user') #se coloca al lado derecho lo que se quiere filtrar
    inlines = (MembershipInline, ) #Coloca un formulario dentro de otro
admin.site.register(Venta,VentaAdmin) #Aquí registro lo que quiero que se observe en el navegador

