from django.db import models
from django.contrib.auth.models import User
from apps.vehiculos.models import Vehiculo
# Create your models here.

class Venta(models.Model):
    fecha = models.DateField()
    ValorTotal =models.BigIntegerField()
    tipoPago =models.CharField(max_length=20)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    vehiculo = models.ManyToManyField(Vehiculo, through='VehiculoVenta') #through indica el modelo de esa relacion, le puse el nombre de VehiculoVenta y debo crear esa clase

 

class VehiculoVenta(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, blank=False, null=False, on_delete=models.CASCADE)#Cuando la relacion es de unos a muchos le pongo foreign key
    venta = models.ForeignKey(Venta, blank=False, null=False, on_delete=models.CASCADE)#Cuando la relacion es de unos a muchos le pongo foreign key
    cantidad= models.IntegerField() #aparte de los campos obligatorios: llaves foráneas, puedo agregar mas campos como precio y cantidad
    precio=models.BigIntegerField()