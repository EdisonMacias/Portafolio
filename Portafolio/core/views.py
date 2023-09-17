from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from.models import About,Especialidad

# Create your views here.

class home(TemplateView):
    template_name = 'core/index.html'
    def get(selt, request):
        about = About.objects.all()
        espe = Especialidad.objects.all()
        return render(request, selt.template_name, {'about':about, 'espe':espe})
    
class Servicio(TemplateView):
    template_name = 'core/Servicios.html'
    def get(selt, request):
        return render(request, selt.template_name)
    
class Trabajos(TemplateView):
    template_name = 'core/Trabajos.html'
    def get(selt, request):
        return render(request, selt.template_name)
    
class Contacto(TemplateView):
    template_name = 'core/Contacto.html'
    def get(selt, request):
        return render(request, selt.template_name)