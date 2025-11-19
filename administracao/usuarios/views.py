from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def cadastro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Verifique os dados informados.')
    else:
        form = UserRegistrationForm()

    return render(request, 'cadastro.html', {'form': form})
