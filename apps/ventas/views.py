from django.shortcuts import render, redirect
from apps.ventas.models import Venta, VehiculoVenta, Usuario
from apps.ventas.formVenta import VentaForm
from apps.ventas.formVehiculoVenta import VehiculoVentaForm
from apps.ventas.formUsuario import UsuarioForm

def listVentas(request):
    ventas = Venta.objects.all().order_by('-id') 
    context = {'ventas':ventas} 
    return render(request, 'ventas/listVentas.html', context)

def home (request):
    return render(request, 'base/base.html')

def ventaCreate(request):
    if request.method == 'POST':
        form = VentaForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listVentas')
    else:
        form =VentaForm()
        return render(request,'ventas/venta_form.html', {'form': form})

def ventaEdit(request, id_venta):
    venta = Venta.objects.get(pk=id_venta)

    if request.method == 'GET':
        form = VentaForm(instance=venta)
    else:
        form =VentaForm(request.POST, instance=venta) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listVentas') 

    return render(request,'ventas/venta_form.html', {'form': form})
 
def ventaEliminar(request, id_venta):
    venta = Venta.objects.get(pk=id_venta)

    if request.method == 'POST':
       venta.delete()
       return redirect('ventas:listVentas')
    return render(request,'ventas/ventaEliminar.html', {'venta': venta})

#-------------Vehiculo Venta
def listVehiculoVentas(request):
    vehiculoVentas = VehiculoVenta.objects.all().order_by('-id') 
    context = {'ventas':vehiculoVentas} 
    return render(request, 'vehiculoVentas/listVehiculoVentas.html', context) 


def vehiculoVentasCreate(request):
    if request.method == 'POST':
        form = VehiculoVentaForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listVehiculoVentas')
    else:
        form =VehiculoVentaForm()
        return render(request,'vehiculoVentas/vehiculoVentas_form.html', {'form': form})

def vehiculoVentasEdit(request, id_vehiculoVenta):
    vehiculoVentas = VehiculoVenta.objects.get(pk=id_vehiculoVenta)

    if request.method == 'GET':
        form = VehiculoVentaForm(instance=vehiculoVentas)
    else:
        form =VehiculoVentaForm(request.POST, instance=vehiculoVentas) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listVehiculoVentas') #el enlace que puse en base.html cuando va a vehiculos

    return render(request,'vehiculoVentas/vehiculoVentas_form.html', {'form': form})
 
def vehiculoVentasEliminar(request, id_venta):
    vehiculoVentas = VehiculoVenta.objects.get(pk=id_venta)

    if request.method == 'POST':
       vehiculoVentas.delete()
       return redirect('ventas:listVehiculoVentas')
    return render(request,'vehiculoVentas/vehiculoVentasEliminar.html', {'vehiculoVentas': vehiculoVentas})

#-------------Usuario -----------

def listUsuarios(request):
    usuarios = Usuario.objects.all().order_by('-id') 
    context = {'ventas':usuarios} 
    return render(request, 'usuarios/listUsuarios.html', context) 


def usuariosCreate(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listUsuarios')
    else:
        form =UsuarioForm()
        return render(request,'usuarios/usuario_form.html', {'form': form})

def usuariosEdit(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)

    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)
    else:
        form =UsuarioForm(request.POST, instance=usuario) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listUsuarios') 

    return render(request,'usuarios/usuario_form.html', {'form': form})
 
def usuariosEliminar(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)

    if request.method == 'POST':
       usuario.delete()
       return redirect('ventas:listUsuarios')
    return render(request,'usuarios/usuarioEliminar.html', {'usuarios': usuario})

   