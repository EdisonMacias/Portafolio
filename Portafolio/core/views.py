from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from.models import About, Portafolio

# Create your views here.

class home(TemplateView):
    template_name = 'core/index.html'
    def get(self, request):
        about = get_object_or_404(About)
        espe = about.especialidad_set.all()
        leng = about.lenguaje_set.all()
        return render(request, self.template_name, {'about':about, 'espe':espe, 'leng':leng})
    
class Servicio(TemplateView):
    template_name = 'core/Servicios.html'
    def get(self, request):
        about = get_object_or_404(About)
        svc = about.servicio_set.all()
        return render(request, self.template_name,{'svc':svc})
    
class Trabajos(TemplateView):
    template_name = 'core/Trabajos.html'
    def get(self, request): 
        portfolio = Portafolio.objects.all()
        return render(request, self.template_name, {'portfolio':portfolio})
    
class Trabajo_detalle(TemplateView):
    template_name = 'core/Trabajos-detalle.html'
    def get(self, request, nombre): 
        portfolio = Portafolio.objects.filter(nom=nombre)
        return render(request, self.template_name, {'portfolio':portfolio})
    
class Contacto(TemplateView):
    template_name = 'core/Contacto.html'
    def get(self, request):
        about = get_object_or_404(About)
        contacto = about.contacto_set.all()
        return render(request, self.template_name,{'about':about, 'contacto':contacto})