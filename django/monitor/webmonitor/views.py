from webmonitor.models import Registros,Relaciones,Sensores
from webmonitor.serializers import *
from django.http import HttpResponse
from rest_framework import viewsets
from django.template import RequestContext, loader
from rest_framework import generics
from django.core import serializers
from logic import *
# Create your views here.
def index(request):
	template = loader.get_template('webmonitor/index.html',)
	return HttpResponse(template.render())
def dashboard(request):
	sensores = DashboardLogic();

	sensores = list(sensores);
	template = loader.get_template('webmonitor/dashboard.html')
	return HttpResponse(template.render(locals()))

def graficas(request):
	sensores = GraficasLogic();
	template = loader.get_template('webmonitor/graficas.html')
	return HttpResponse(template.render(locals()))

#API
class RelacionesViewSet (viewsets.ModelViewSet):
	serializer_class = RelacionesSerializer
	queryset = Relaciones.objects.all()

class SensoresViewSet (viewsets.ModelViewSet):
	serializer_class = SensoresSerializer
	queryset = Sensores.objects.all()

class RegistrosViewSet(viewsets.ModelViewSet):
	serializer_class = RegistrosSerializer
	def get_queryset(self):
		kwargs = self.kwargs
		if len(kwargs) > 0:
			print kwargs
			sensor_id = kwargs['sensor_id']
			return Registros.objects.filter(sensor_id=sensor_id).order_by('-fecha')
		else:
			return Registros.objects.all().order_by('-fecha')
		