from django.urls import path
from .views import home, Servicio, Trabajos, Contacto, Trabajo_detalle

urlpatterns = [
    path('',home.as_view(),name="home"),
    path('Servicios',Servicio.as_view(),name="Servicios"),
    path('Trabajos',Trabajos.as_view(),name="Trabajos"),
    path('Trabajo_detalle/<nombre>',Trabajo_detalle.as_view(),name="Trabajo_detalle"),
    path('Contacto',Contacto.as_view(),name="Contacto")
]


