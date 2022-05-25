from django.contrib import admin
from django.urls import path, include
from apps.vehiculos.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('vehiculos/', include('apps.vehiculos.urls', namespace='vehiculos')), 
    path('ventas/', include('apps.ventas.urls', namespace='ventas')), 
]
