from webmonitor.models import Registros
from webmonitor.serializers import *
from django.http import HttpResponse
from rest_framework import viewsets
from django.template import RequestContext, loader
from rest_framework import generics

# Create your views here.
def index(request):
	template = loader.get_template('webmonitor/index.html')
	return HttpResponse(template.render())
def dashboard(request):
	template = loader.get_template('webmonitor/dashboard.html')
	return HttpResponse(template.render())

class RegistrosList(generics.ListAPIView):
	serializer_class = RegistrosSerializer
	queryset = Registros.objects.all()
	def get_queryset(self):
		sensor_id = self.kwargs['sensor_id']
		return Registros.objects.filter(sensor_id=sensor_id)
class RegistrosViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	serializer_class = RegistrosSerializer
	sensor_id = 2
	# Registros.objects.all().order_by('-fecha')
	def get_queryset(self):
		kwargs = self.kwargs
		if len(kwargs) > 0:
			print kwargs
			sensor_id = kwargs['sensor_id']
			return Registros.objects.filter(sensor_id=sensor_id).order_by('-fecha')
		else:
			return Registros.objects.all().order_by('-fecha')
		