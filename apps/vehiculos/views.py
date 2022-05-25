from django.shortcuts import render, redirect
from apps.vehiculos.models import Vehiculo, Marca, TipoVehiculo 
from apps.vehiculos.formVehiculo import VehiculoForm
from apps.vehiculos.formMarca import MarcaForm
from apps.vehiculos.formTipoVehiculo import TipoVehiculosForm


def listVehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('-id') # ordena de forma descendente por el id
    context = {'vehiculos':vehiculos} # creo una variable que se llama vehiculos: y luego a esa variable le asigno la lista de todos los vehiculos y esa se llama vehiculos, la que creé anteriormente
    #context contiene el listado de los vehiculos
    return render(request, 'vehiculos/listVehiculos.html', context) #aquí estoy renderizando, luego en '' pongo la pagina html que crearé para mostrar esta vista y luego le mando el contexto, que es context

def home (request):
    return render(request, 'base/base.html')

def vehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST) #clase que importo desde el archivo formVehiculo.py
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listVehiculos') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =VehiculoForm()
        return render(request,'vehiculos/vehiculo_form.html', {'form': form})

def vehiculoEdit(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(pk=id_vehiculo)

    if request.method == 'GET':
        form = VehiculoForm(instance=vehiculo)
    else:
        form =VehiculoForm(request.POST, instance=vehiculo) 
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listVehiculos') #el enlace que puse en base.html cuando va a vehiculos

    return render(request,'vehiculos/vehiculo_form.html', {'form': form})
 
def vehiculoEliminar(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(pk=id_vehiculo)

    if request.method == 'POST':
       vehiculo.delete()
       return redirect('vehiculos:listVehiculos')
    return render(request,'vehiculos/vehiculoEliminar.html', {'vehiculo': vehiculo})   

#----------------- Marcas

def listMarcas(request):
    marcas = Marca.objects.all().order_by('-id') # ordena de forma descendente por el id
    context = {'vehiculos':marcas} # creo una variable que se llama vehiculos: y luego a esa variable le asigno la lista de todos los vehiculos y esa se llama vehiculos, la que creé anteriormente
    #context contiene el listado de los vehiculos
    return render(request, 'marcas/listMarcas.html', context) #aquí estoy renderizando, luego en '' pongo la pagina html que crearé para mostrar esta vista y luego le mando el contexto, que es context

def marcaCreate(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST) #clase que importo desde el archivo formVehiculo.py
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listMarcas') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =MarcaForm()
        return render(request,'marcas/marca_form.html', {'form': form})

def marcaEdit(request, id_marca):
    marca = Marca.objects.get(pk=id_marca)

    if request.method == 'GET':
        form = MarcaForm(instance=marca)
    else:
        form =MarcaForm(request.POST, instance=marca) 
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listMarcas') #el enlace que puse en base.html cuando va a vehiculos

    return render(request,'marcas/marca_form.html', {'form': form})
 
def marcaEliminar(request, id_marca):
    marca = Marca.objects.get(pk=id_marca)

    if request.method == 'POST':
       marca.delete()
       return redirect('vehiculos:listMarcas')
    return render(request,'marcas/marcaEliminar.html', {'marca': marca})   


#----------------- Tipo Vehiculo

def listTipoVehiculo(request):
    tipoVehiculos = TipoVehiculo.objects.all().order_by('-id') 
    context = {'vehiculos':tipoVehiculos} 
    return render(request, 'tipoVehiculos/listTipoVehiculos.html', context) 

def tipoVehiculosCreate(request):
    if request.method == 'POST':
        form = TipoVehiculosForm(request.POST) #clase que importo desde el archivo formVehiculo.py
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listTipoVehiculo') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =TipoVehiculosForm()
        return render(request,'tipoVehiculos/tipoVehiculos_form.html', {'form': form})

def tipoVehiculosEdit(request, id_tipoVehiculo):
    tipoVehiculos = TipoVehiculo.objects.get(pk=id_tipoVehiculo)
    if request.method == 'GET':
        form = TipoVehiculosForm(instance=tipoVehiculos)
    else:
        form =TipoVehiculosForm(request.POST, instance=tipoVehiculos) 
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listTipoVehiculo') #el enlace que puse en base.html cuando va a vehiculos

    return render(request,'tipoVehiculos/tipoVehiculos_form.html', {'form': form})
 
def tipoVehiculosEliminar(request, id_tipoVehiculo):
    tipoVehiculos = TipoVehiculo.objects.get(pk=id_tipoVehiculo)

    if request.method == 'POST':
       tipoVehiculos.delete()
       return redirect('vehiculos:listTipoVehiculo')
    return render(request,'tipoVehiculos/tipoVehiculosEliminar.html', {'tipoVehiculos': tipoVehiculos})   
