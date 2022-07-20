from django.contrib.auth.models import User, Group
from administrativo.models import Propietario, Departamento

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PropietarioSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Propietario
        fields = '__all__'


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    propietario_str = serializers.StringRelatedField(source="propietario", read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Departamento
        # fields = ['id', 'telefono', 'tipo']
        fields = '__all__'
