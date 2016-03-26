from __future__ import unicode_literals
from django.utils.encoding import force_unicode
from django.db import models

# Create your models here.
class Registros(models.Model):
	id = models.AutoField(primary_key=True)
	sensor_id = models.IntegerField()
	valor = models.FloatField()
	fecha = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return 'Sensor: ' + str(self.sensor_id) + ' Valor: '+str(self.valor)
	class Meta:
		managed = False
		db_table = 'registros'
		verbose_name_plural = 'Registros'

class Relaciones(models.Model):
	id = models.AutoField(primary_key=True)
	id1 = models.IntegerField()
	id2 = models.IntegerField()
	def __unicode__(self):
		return 'ID1: ' + str(self.id1) + ' ID2: '+str(self.id2)
	class Meta:
		managed = False
		db_table = 'relaciones'
		verbose_name_plural = 'Relaciones'

class Sensores(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=45)
	unidad = models.CharField(max_length=4)
	graficas = models.IntegerField()
	icon = models.CharField(max_length=40)
	actualizable = models.IntegerField()
	maxmin = models.IntegerField()
	def __unicode__(self):
		return 'ID: ' + str(self.id) + ' Nombre: '+str(self.name)
	class Meta:
		managed = False
		db_table = 'sensores'
		verbose_name_plural = 'Sensores'

class FacebookUsers(models.Model):
	"""docstring for FacebookUsers"""
	id = models.AutoField(primary_key=True)
	fbid = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	token = models.CharField(max_length=255)
	def __unicode__(self):
		return  force_unicode(self.name)
	class Meta:
		managed = False
		db_table = 'facebook_users'
		verbose_name_plural = 'Facebook Users'

class TelegramUsers(models.Model):
	"""docstring for TelegramUsers"""
	id = models.AutoField(primary_key=True)
	userID = models.CharField(max_length=255)
	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	def __unicode__(self):
		return str(self.username)
	class Meta:
		managed = False
		db_table = 'telegram_users'
		verbose_name_plural = 'Telegram Users'
		