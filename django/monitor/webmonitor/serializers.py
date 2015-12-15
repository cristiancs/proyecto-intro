from webmonitor.models import Registros,Relaciones,Sensores
from rest_framework import serializers


class RegistrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registros
        fields = ('sensor_id', 'valor', 'fecha')

class RelacionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relaciones
        fields = ('id1', 'id2')

class SensoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensores
        fields = ('id', 'name', 'unidad', 'graficas', 'icon', 'actualizable', 'maxmin')
 