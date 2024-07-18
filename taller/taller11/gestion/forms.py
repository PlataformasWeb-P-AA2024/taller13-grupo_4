# gestion/forms.py

from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from gestion.models import Edificio, Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese la dirrecion por favor'),
            'ciudad': _('Ingrese la ciudad por favor'),
            'tipo': _('Ingrese el tipo por favor'),
        }

    def clean_ciudad(self):
        ciudad = self.cleaned_data['ciudad']
        if ciudad.startswith('L'):
            raise forms.ValidationError("El nombre de la ciudad no puede comenzar con 'L'.")
        return ciudad

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'numero_cuartos', 'edificio']

    def clean_costo(self):
        costo = self.cleaned_data['costo']
        if costo > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a $100,000.")
        return costo

    def clean_numero_cuartos(self):
        numero_cuartos = self.cleaned_data['numero_cuartos']
        if numero_cuartos < 1 or numero_cuartos > 7:
            raise forms.ValidationError("El número de cuartos debe estar entre 1 y 7.")
        return numero_cuartos

    def clean_nombre_propietario(self):
        nombre_propietario = self.cleaned_data['nombre_propietario']
        if len(nombre_propietario.split()) < 3:
            raise forms.ValidationError("El nombre del propietario debe tener al menos 3 palabras.")
        return nombre_propietario

class DepartamentoEdificioForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'numero_cuartos', 'edificio']

    def __init__(self, edificio, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.HiddenInput()

    def clean_costo(self):
        costo = self.cleaned_data['costo']
        if costo > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a $100,000.")
        return costo

    def clean_numero_cuartos(self):
        numero_cuartos = self.cleaned_data['numero_cuartos']
        if numero_cuartos < 1 or numero_cuartos > 7:
            raise forms.ValidationError("El número de cuartos debe estar entre 1 y 7.")
        return numero_cuartos

    def clean_nombre_propietario(self):
        nombre_propietario = self.cleaned_data['nombre_propietario']
        if len(nombre_propietario.split()) < 3:
            raise forms.ValidationError("El nombre del propietario debe tener al menos 3 palabras.")
        return nombre_propietario
