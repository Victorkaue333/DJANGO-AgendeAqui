from django.urls import path
from . import views

app_name = 'agendamentos'

urlpatterns = [
    path('', views.agendamentos, name='agendamentos'),
]