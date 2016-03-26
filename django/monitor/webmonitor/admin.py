from django.contrib import admin

from .models import *
admin.site.register(Registros)
admin.site.register(Relaciones)
admin.site.register(Sensores)
admin.site.register(FacebookUsers)
admin.site.register(TelegramUsers)

# Register your models here.
