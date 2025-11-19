from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seu usuário',
                'id': 'id_username',
                'autofocus': 'autofocus',
                'autocomplete': 'username'
            }
        )
    )

    password = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Sua senha',
                'id': 'id_password',
                'autocomplete': 'current-password'
            }
        )
    )


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seu usuário',
                'id': 'id_username',
                'autofocus': 'autofocus',
                'autocomplete': 'username'
            }
        )
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'seu@email.com',
                'id': 'id_email',
                'autocomplete': 'email'
            }
        )
    )

    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '********',
                'id': 'id_password1',
                'autocomplete': 'new-password'
            }
        )
    )

    password2 = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '********',
                'id': 'id_password2',
                'autocomplete': 'new-password'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail já cadastrado.')
        return email
