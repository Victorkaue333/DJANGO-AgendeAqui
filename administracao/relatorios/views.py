from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from django.utils.encoding import smart_str
import csv

def index(request):
    # Relatório genérico: lista salas e tenta carregar agendamentos se existir
    salas = []
    blocos = []
    try:
        from salas.models import Sala, Bloco
        blocos = Bloco.objects.all()
        salas_qs = Sala.objects.select_related('bloco').prefetch_related('recursos')
        bloco_id = request.GET.get('bloco')
        if bloco_id:
            salas_qs = salas_qs.filter(bloco_id=bloco_id)
        salas = list(salas_qs)
    except Exception:
        salas = []
        blocos = []

    agendamentos = None
    ag_count = None
    try:
        from agendamentos.models import Agendamento
        qs = Agendamento.objects.all()
        start = request.GET.get('start')
        end = request.GET.get('end')
        if start:
            qs = qs.filter(data__gte=start)
        if end:
            qs = qs.filter(data__lte=end)
        agendamentos = qs.select_related('usuario', 'sala')
        ag_count = agendamentos.count()
    except Exception:
        agendamentos = None
        ag_count = None

    # Dados para gráfico: salas por bloco
    chart_data = []
    try:
        counts = (
            __import__('django').db.models.query.QuerySet
        )
        # safer: compute from Sala if available
        if salas:
            d = {}
            for s in salas:
                key = s.bloco.nome if s.bloco else 'Sem bloco'
                d[key] = d.get(key, 0) + 1
            chart_data = [{'label': k, 'value': v} for k, v in d.items()]
    except Exception:
        chart_data = []

    context = {
        'salas': salas,
        'blocos': blocos,
        'agendamentos': agendamentos,
        'ag_count': ag_count,
        'chart_data': chart_data,
    }
    return render(request, 'relatorios/index.html', context)


def export_csv(request):
    # Se houver Agendamento, exporta agendamentos filtrados; caso contrário exporta salas
    try:
        from agendamentos.models import Agendamento
        qs = Agendamento.objects.all()
        start = request.GET.get('start')
        end = request.GET.get('end')
        if start:
            qs = qs.filter(data__gte=start)
        if end:
            qs = qs.filter(data__lte=end)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="agendamentos.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Data', 'Horário Início', 'Horário Fim', 'Sala', 'Usuário', 'Motivo', 'Status'])
        for a in qs:
            writer.writerow([
                a.id,
                smart_str(getattr(a, 'data', '')),
                smart_str(getattr(a, 'horario_inicio', '')),
                smart_str(getattr(a, 'horario_fim', '')),
                smart_str(getattr(a, 'sala', '')),
                smart_str(getattr(a, 'usuario', '')),
                smart_str(getattr(a, 'motivo', '')),
                smart_str(getattr(a, 'status', '')),
            ])
        return response
    except Exception:
        # Exporta salas como fallback
        try:
            from salas.models import Sala
            qs = Sala.objects.select_related('bloco').prefetch_related('recursos')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="salas.csv"'
            writer = csv.writer(response)
            writer.writerow(['ID', 'Nome', 'Bloco', 'Capacidade', 'Recursos'])
            for s in qs:
                recursos = ', '.join([r.nome for r in s.recursos.all()])
                writer.writerow([s.id, s.nome, s.bloco.nome if s.bloco else '', s.capacidade, recursos])
            return response
        except Exception:
            return HttpResponse('Nenhum dado disponível para exportação.', status=400)
