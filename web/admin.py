from os import name
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ['nome']
    
@admin.register(TipoLocal)
class TipoLocalAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Beacon)
class BeaconAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Locais)
class EspacoAdmin(admin.ModelAdmin):
    list_display = ['local']

@admin.register(Espacos)
class EspacosAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Percurso)
class PercursoAdmin(admin.ModelAdmin):
    list_display = ['id']