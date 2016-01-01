from django.utils import timezone
import datetime
from django.db.models import Max,Min
from webmonitor.models import Registros,Relaciones,Sensores

def DashboardLogic():
	data = list()
	relaciones = Relaciones.objects.all().values('id2')
	# print relaciones
	# relaciones = [1,2]
	sensores = Sensores.objects.exclude(id__in=relaciones)
	sensores = sensores.values()
	# print sensores;
	for sensor in sensores:
		data.append(dict())
		actualdata = data[-1]
		#Registramos Valores Basicos
		for name,value in sensor.items():
			data[-1][name]=value
		#Registramos la ultima medicion del sensor principal
		actualdata['registros'] = list()
		registro1 = Registros.objects.filter(sensor_id=sensor['id']).values().last()

		actualdata['registros'].append((registro1,sensor['icon'],sensor['unidad'],sensor['id']));

		#Verificamos si se relaciona con otro sensor
		relacion = Relaciones.objects.filter(id1=sensor['id']).values()
		if(relacion.count() > 0):
			#obtener info del sensor 2:
			sensor2 = Sensores.objects.filter(id=relacion[0]['id2']).values()
			#registramos la medicion del sensor 2
			registro2 = Registros.objects.filter(sensor_id=relacion[0]['id2']).values().last()
			# print sensor2[0]['id']
			if(registro2):
				actualdata['registros'].append((registro2,sensor2[0]['icon'],sensor2[0]['unidad'],relacion[0]['id2']));
		actualdata['relacion'] = True
		#Determinamos maximos y minimos diarios del principal
		if(sensor["maxmin"] == 1):
			maxima = Registros.objects.filter(sensor_id=sensor['id'],fecha__startswith=datetime.date.today()).aggregate(Max('valor')).values()
			minima = Registros.objects.filter(sensor_id=sensor['id'],fecha__startswith=datetime.date.today()).aggregate(Min('valor')).values()
			print maxima,minima
			if(maxima[0] == None):
				maxima = '-'
			else:
				maxima=round(maxima[0],2)
			if(minima[0] == None):
				minima = '-'
			else:
				minima=round(minima[0],2)
			# print maxima,minima
		actualdata['max'] = maxima
		actualdata['min'] = minima
	return data

def GraficasLogic():
	sensores = Sensores.objects.filter(graficas=1).values()
	return sensores