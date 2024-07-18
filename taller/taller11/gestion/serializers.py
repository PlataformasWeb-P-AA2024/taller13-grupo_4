from rest_framework import serializers
from django.contrib.auth.models import User, Group
from gestion.models import Edificio, Departamento


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = '__all__'

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

from rest_framework import serializers

