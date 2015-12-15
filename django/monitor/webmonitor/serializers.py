from webmonitor.models import Registros
from rest_framework import serializers


class RegistrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registros
        fields = ('sensor_id', 'valor', 'fecha')

