from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    
class Lenguaje(models.Model):
    Leng = models.CharField(max_length=100, verbose_name="Lenguajes")
    porc = models.IntegerField(verbose_name="Porcentaje", validators=[
            MinValueValidator(0, message="El valor no puede ser menor que 0."),
            MaxValueValidator(100, message="El valor no puede ser mayor que 100.")
        ])
    about = models.ManyToManyField(About)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Lenguaje'
        verbose_name_plural = 'Lenguajes'
        ordering = ["-created"]
    def __str__(self):
        return self.Leng
    
class Contacto(models.Model):
    msj = models.TextField(verbose_name="Mensaje")
    drc = models.CharField(max_length=200, verbose_name="Direccion")
    fcb = models.URLField(max_length=300, verbose_name="Enlace a Facebook")
    itg = models.URLField(max_length=300, verbose_name="Enlace a Instagram")
    wsp = models.URLField(max_length=300, verbose_name="Enlace a Whatsapp")
    about = models.ManyToManyField(About)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ["-created"]
    def __str__(self):
        return self.drc
    
class Servicio(models.Model):
    svc = models.CharField(max_length=150, verbose_name="Nombre del servicio")
    dcpc = models.TextField(verbose_name="Descripcion")
    icon = models.CharField(max_length=50, verbose_name="Icono")
    about = models.ManyToManyField(About)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ["-created"]
    def __str__(self):
        return self.svc
    
class Portafolio(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nombre del proyecto")
    tipo = models.CharField(max_length=100, verbose_name="Tipo de proyecto")
    cliente = models.CharField(max_length=100, verbose_name="Cliente")
    fecha = models.DateField(verbose_name="Fecha de creacion")
    url = models.URLField(null=True, blank=True, verbose_name="URL", max_length=300)
    detall = models.TextField(verbose_name="Detalle")
    img1 = models.ImageField(verbose_name="Imagen 1", upload_to='img/')
    img2 = models.ImageField(verbose_name="Imagen 2", upload_to='img/')
    img3 = models.ImageField(verbose_name="Imagen 3", upload_to='img/')
    about = models.ManyToManyField(About)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'
        ordering = ["-created"]
    def __str__(self):
        return self.nom
    