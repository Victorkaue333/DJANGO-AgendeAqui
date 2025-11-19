
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='root_login'),
    path('dashboard/', include('dashboard.urls')),
    path('salas/', include('salas.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('agendamentos/', include('agendamentos.urls')),
]
