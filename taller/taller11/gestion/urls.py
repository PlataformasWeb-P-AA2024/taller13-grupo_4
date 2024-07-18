from django.urls import path, include
from rest_framework import routers
from . import views
from .views import EdificioViewSet, DepartamentoViewSet

router = routers.DefaultRouter()
router.register(r'edificios', EdificioViewSet)
router.register(r'departamentos', DepartamentoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('obtenerEdificio/<int:id>/', views.obtener_edificio, name='obtener_edificio'),
    path('editarEdificio/<int:id>/', views.editar_edificio, name='editar_edificio'),
    path('eliminarEdificio/<int:id>/', views.eliminar_edificio, name='eliminar_edificio'),
    path('editarDepartamento/<int:id>/', views.editar_departamento, name='editar_departamento'),
    path('crearDepartamentoEdificio/<int:id>/', views.crear_departamento_edifico, name='crear_departamento_edificio'), 
    path('listarEdificios/', views.listar_edificios, name='listar_edificios'),  
    path('crearEdificio/', views.crear_edificio, name='crear_edificio'),
    path('crearDepartamentoEdificio/<int:id>/', views.crear_departamento_edifico, name='crear_departamento_edificio'), 
    path('listarDepartamentos/', views.listar_departamentos, name='listar_departamentos'),
    path('crearDepartamento/', views.crear_departamento, name='crear_departamento'),
    path('editarDepartamento/<int:id>/', views.editar_departamento, name='editar_departamento'),
    path('eliminarDepartamento/<int:id>/', views.eliminar_departamento, name='eliminar_departamento'),
    
    # Incluye las rutas de la API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
