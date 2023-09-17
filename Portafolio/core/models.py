from django.db import models

# Create your models here.
class About(models.Model):
    Nom = models.CharField(max_length=100, verbose_name="Nombres")
    Apell = models.CharField(max_length=100, verbose_name="Apellidos")
    Tit = models.CharField(max_length=100, verbose_name="Titulo")
    perfil = models.CharField(max_length=100, verbose_name="Perfil")
    tel = models.CharField(max_length=100, verbose_name="Telefono")
    email = models.CharField(max_length=100, verbose_name="Email")
    Descrip = models.TextField(verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Acerca de mi'
        verbose_name_plural = 'Acerca de mi'
        ordering = ["-created"]
    def __str__(self):
        return self.Nom

class Especialidad(models.Model):
    Espe = models.CharField(max_length=100, verbose_name="Especialidad")
    about = models.ManyToManyField(About)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        ordering = ["-created"]
    def __str__(self):
        return self.Espe