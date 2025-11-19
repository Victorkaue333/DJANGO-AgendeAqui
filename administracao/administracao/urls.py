
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from usuarios.forms import CustomAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', TemplateView.as_view(template_name='landinpage.html'), name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('salas/', include('salas.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('agendamentos/', include('agendamentos.urls')),
    path('', include('usuarios.urls')),
]
