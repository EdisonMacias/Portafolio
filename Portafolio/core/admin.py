from django.contrib import admin
from .models import About, Especialidad

class Admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(About, Admin)
admin.site.register(Especialidad, Admin)
