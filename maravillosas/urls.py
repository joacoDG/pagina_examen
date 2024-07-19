from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [

    path('', views.index, name='index'),
    path('inicio/',views.inicio, name='inicio' ),
    path('Contacto/',views.contacto, name='Contacto'),
    path('Login/',views.login, name='Login'),
    path('Registro/',views.registro, name='Registro'),
    path('Accesorios/',views.accesorios, name='Accesorios')
    
]