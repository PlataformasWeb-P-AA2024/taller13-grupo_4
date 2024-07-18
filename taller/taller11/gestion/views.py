from rest_framework import viewsets

from django.shortcuts import render, redirect, get_object_or_404
from .models import Edificio, Departamento
from .forms import EdificioForm, DepartamentoForm, DepartamentoEdificioForm

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from gestion.serializers import UserSerializer, GroupSerializer, \
EdificioSerializer, DepartamentoSerializer


from django.contrib.auth.models import User, Group
from rest_framework import permissions

# Vistas basadas en funciones de Django
def index(request):
    edificios = Edificio.objects.all()
    informacion_template = {'edificios': edificios, 'numero_edificios': len(edificios)}
    return render(request, 'index.html', informacion_template)

def obtener_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    informacion_template = {'edificio': edificio}
    return render(request, 'obtenerEdificio.html', informacion_template)

def crear_edificio(request):
    if request.method == 'POST':
        formulario = EdificioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm()
    informacion_template = {'formulario': formulario}
    return render(request, 'crearEdificio.html', informacion_template)

def editar_edificio(request, id):
    edificio = get_object_or_404(Edificio, pk=id)
    if request.method == 'POST':
        form = EdificioForm(request.POST, instance=edificio)
        if form.is_valid():
            form.save()
            return redirect('listar_edificios')
    else:
        form = EdificioForm(instance=edificio)
    return render(request, 'editarEdificio.html', {'form': form})

def eliminar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

def listar_edificios(request):
    edificios = Edificio.objects.all()
    informacion_template = {'edificios': edificios, 'numeroEdificios': len(edificios)}
    return render(request, 'listarEdificios.html', informacion_template)

def crear_departamento(request):
    if request.method == 'POST':
        formulario = DepartamentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    informacion_template = {'formulario': formulario}
    return render(request, 'crearDepartamento.html', informacion_template)

def crear_departamento_edifico(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = DepartamentoEdificioForm(edificio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoEdificioForm(edificio)
    informacion_template = {'formulario': formulario, 'edificio': edificio}
    return render(request, 'crearDepartamentoEdificio.html', informacion_template)

def editar_departamento(request, id):
    departamento = get_object_or_404(Departamento, pk=id)
    if request.method == 'POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_departamentos')
    else:
        formulario = DepartamentoForm(instance=departamento)
    return render(request, 'editarDepartamento.html', {'form': formulario})

def eliminar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    informacion_template = {'departamentos': departamentos, 'numeroDepartamentos': len(departamentos)}
    return render(request, 'listarDepartamentos.html', informacion_template)

# Vistas basadas en Viewsets de Django Rest Framework
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EdificioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows buildings to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed or edited.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    # permission_classes = [permissions.IsAuthenticated]
