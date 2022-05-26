from django.db import models
from apps.vehiculos.models import Vehiculo

class Usuario(models.Model):
    nombres=models.CharField(verbose_name="Nombres", max_length=70)
    tipoIdentificacion=models.CharField(verbose_name="Tipo de Identificación", max_length=20)
    num_identificacion=models.BigIntegerField(verbose_name="Número de Identificación")
    telefono = models.BigIntegerField(verbose_name="Teléfono")
    direccion = models.CharField(verbose_name="Dirección", max_length=40)

    def __str__(self):
        return self.nombres

class Venta(models.Model):
    tipoPago_choices=(
        ('Efectivo','Efectivo'),
        ('Crédito','Crédito'),
    )
    fecha = models.DateField()
    ValorTotal =models.BigIntegerField(verbose_name="Valor Total")
    tipoPago =models.CharField(max_length=20, verbose_name="Tipo de Pago", choices=tipoPago_choices, default='efectivo')
    user = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuario")
    vehiculo = models.ManyToManyField(Vehiculo, through='VehiculoVenta') #through indica el modelo de esa relacion, le puse el nombre de VehiculoVenta y debo crear esa clase

    def __str__(self):
        return str (self.id)
    

class VehiculoVenta(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, blank=False, null=False, on_delete=models.CASCADE)#Cuando la relacion es de unos a muchos le pongo foreign key
    venta = models.ForeignKey(Venta, blank=False, null=False, on_delete=models.CASCADE)#Cuando la relacion es de unos a muchos le pongo foreign key
    cantidad= models.IntegerField() #aparte de los campos obligatorios: llaves foráneas, puedo agregar mas campos como precio y cantidad
    precio=models.BigIntegerField()
    
    def __str__(self):
        return "%s %s" %(self.cantidad, self.precio)