from django.urls import path
from .views import home, Servicio, Trabajos, Blog, Contacto

urlpatterns = [
    path('',home.as_view(),name="home"),
    path('Servicios',Servicio.as_view(),name="Servicios"),
    path('Trabajos',Trabajos.as_view(),name="Trabajos"),
    path('Blog',Blog.as_view(),name="Blog"),
    path('Contacto',Contacto.as_view(),name="Contacto")
]


