from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registros(models.Model):
	id = models.AutoField(primary_key=True)
	sensor_id = models.IntegerField()
	valor = models.FloatField()
	fecha = models.DateTimeField(auto_now_add=True)

	class Meta:
		managed = False
		db_table = 'registros'

class Relaciones(models.Model):
	id = models.AutoField(primary_key=True)
	id1 = models.IntegerField()
	id2 = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'relaciones'

class Sensores(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=45)
	unidad = models.CharField(max_length=4)
	graficas = models.IntegerField()
	icon = models.CharField(max_length=40)
	actualizable = models.IntegerField()
	maxmin = models.IntegerField()
	class Meta:
		managed = False
		db_table = 'sensores'