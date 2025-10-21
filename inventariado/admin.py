from django.contrib import admin
from .models import Ubicaciones, Dispositivos, Traslados

admin.site.register(Ubicaciones)
admin.site.register(Dispositivos)
admin.site.register(Traslados)