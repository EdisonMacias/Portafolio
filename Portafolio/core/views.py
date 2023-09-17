from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
class home(TemplateView):
    template_name = 'core/index.html'
    def get(selt, request):
        return render(request, selt.template_name)
    
@csrf_protect
class Servicio(TemplateView):
    template_name = 'core/Servicios.html'
    def get(selt, request):
        return render(request, selt.template_name)

@csrf_protect 
class Trabajos(TemplateView):
    template_name = 'core/Trabajos.html'
    def get(selt, request):
        return render(request, selt.template_name)
@csrf_protect    
class Blog(TemplateView):
    template_name = 'core/Blog.html'
    def get(selt, request):
        return render(request, selt.template_name)
@csrf_protect
class Contacto(TemplateView):
    template_name = 'core/Contacto.html'
    def get(selt, request):
        return render(request, selt.template_name)