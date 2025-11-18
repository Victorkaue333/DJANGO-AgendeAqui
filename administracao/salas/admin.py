from django.contrib import admin
from .models import Bloco, Recurso, Sala


@admin.register(Bloco)
class BlocoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'bloco', 'capacidade')
    list_filter = ('bloco',)
    search_fields = ('nome',)
