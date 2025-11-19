# View simples para exibir a página de agendamentos
from django.shortcuts import render

def agendamentos(request):
	return render(request, 'agendamentos/agendamentos.html')
from django.shortcuts import render

# Create your views here.
