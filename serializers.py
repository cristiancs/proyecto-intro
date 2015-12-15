from django.contrib.auth.models import User, Group
from rest_framework import serializers


class RegistrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registros
        fields = ('sensor_id', 'valor', 'fecha')

