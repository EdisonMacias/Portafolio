from django.urls import path
from .views import home, Servicio, Trabajos, Contacto

urlpatterns = [
    path('',home.as_view(),name="home"),
    path('Servicios',Servicio.as_view(),name="Servicios"),
    path('Trabajos',Trabajos.as_view(),name="Trabajos"),
    path('Contacto',Contacto.as_view(),name="Contacto")
]


