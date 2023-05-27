from django.contrib import admin
from .models import Pais, Ciudad, Calle



class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    list_filter = ('pais',)


class CalleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad')
    list_filter = ('ciudad__pais', 'ciudad')