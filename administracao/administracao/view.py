from django.shortcuts import render

def acesso_rapido(request):
	return render(request, 'acesso_rapido.html')

def landinpage(request):
	return render(request, 'landinpage.html')

def login_view(request):
	return render(request, 'login.html')

def cadastro(request):
	return render(request, 'cadastro.html')
