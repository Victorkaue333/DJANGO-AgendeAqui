from django.contrib import admin
from .models import Agendamento


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
	list_display = ('id', 'sala', 'usuario', 'data', 'horario_inicio', 'horario_fim', 'status')
	list_filter = ('status', 'data', 'sala')
	search_fields = ('usuario__username', 'sala__nome', 'motivo')

