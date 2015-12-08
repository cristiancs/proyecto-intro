from django.contrib import admin

from .models import Registros,Relaciones,Sensores
admin.site.register(Registros)
admin.site.register(Relaciones)
admin.site.register(Sensores)

# Register your models here.
