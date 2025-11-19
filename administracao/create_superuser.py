#!/usr/bin/env python
"""Script de conveniência: cria ou atualiza um superuser para testes.

Uso:
  cd administracao
  python create_superuser.py

OBS: Remova ou proteja este arquivo em produção.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'administracao.settings')
django.setup()

from django.contrib.auth import get_user_model

def main():
    User = get_user_model()
    username = 'victoralves'
    password = 'vkau333'
    email = 'victoralves@example.com'

    try:
        user = User.objects.filter(username=username).first()
        if user is None:
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser '{username}' criado com sucesso.")
        else:
            changed = False
            if not user.is_staff:
                user.is_staff = True
                changed = True
            if not user.is_superuser:
                user.is_superuser = True
                changed = True
            if changed:
                user.set_password(password)
                user.save()
                print(f"Usuário existente '{username}' atualizado para superuser e senha definida.")
            else:
                print(f"Usuário '{username}' já é superuser. Nenhuma alteração necessária.")
    except Exception as e:
        print('Erro ao criar/atualizar superuser:', e)

if __name__ == '__main__':
    main()
