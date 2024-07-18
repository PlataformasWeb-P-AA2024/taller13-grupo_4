# gestion/models.py

from django.db import models

class Edificio(models.Model):
    TIPO_CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return "%s %s %d %d" % (self.nombre, self.tipo, self.total_cuartos(), self.total_costo())

    def total_cuartos(self):
        return sum(departamento.numero_cuartos for departamento in self.departamentos.all())

    def total_costo(self):
        return sum(departamento.costo for departamento in self.departamentos.all())

class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=200)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name="departamentos")

    def __str__(self):
        return "%s %d %d %s " % (self.nombre_propietario,self.costo,self.numero_cuartos, self.edificio.nombre)
