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

@admin.register(Espaco)
class EspacoAdmin(admin.ModelAdmin):
    list_display = ['local', 'nome']

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ['local', 'espaco_inicio','espaco_final']

@admin.register(Percurso)
class PercursoAdmin(admin.ModelAdmin):
    list_display = ['local','destino','sequencia']