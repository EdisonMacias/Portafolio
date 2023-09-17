from django.db import models

# Create your models here.
class About (models.Model):
    Nom = models.CharField(max_length=100, verbose_name="Nombres")
    Apell = models.CharField(max_length=100, verbose_name="Apellidos")
    Tit = models.CharField(max_length=100, verbose_name="Titulo")
    Espe = models.ImageField(verbose_name="Imagen", upload_to= "rooms")
    NumPeople = models.IntegerField(verbose_name="Numero de Personas")
    NumRoom = models.IntegerField(verbose_name="Numero de Habitaciones")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Acerca de mi'
        verbose_name_plural = 'Acerca de mi'
        ordering = ["-created"]
    def __str__(self):
        return self.Nom