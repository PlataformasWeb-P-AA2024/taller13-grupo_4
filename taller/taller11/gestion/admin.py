# gestion/admin.py

from django.contrib import admin
from .models import Edificio, Departamento

class DepartamentoInline(admin.TabularInline):
    model = Departamento

class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    inlines = [
        DepartamentoInline,
    ]

admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_propietario', 'costo', 'numero_cuartos', 'edificio')

admin.site.register(Departamento, DepartamentoAdmin)
