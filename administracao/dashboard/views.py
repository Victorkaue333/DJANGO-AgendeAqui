from django.shortcuts import render

def index(request):
    # Para evitar dependência forte em agendamentos (que pode ainda estar vazio), usamos try
    salas_count = 0
    agendamentos_count = 0
    try:
        from salas.models import Sala
        salas_count = Sala.objects.count()
    except Exception:
        salas_count = 0

    try:
        from agendamentos.models import Agendamento
        agendamentos_count = Agendamento.objects.count()
    except Exception:
        agendamentos_count = 0

    context = {
        'salas_count': salas_count,
        'agendamentos_count': agendamentos_count,
    }
    return render(request, 'dashboard/index.html', context)
