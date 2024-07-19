from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#vista pagina de inicio
def index(request):
    return render(request, 'maravillosas/inicio.html')

def inicio(request):
    return render(request, 'incio.html')

def contacto(request):
    return render(request, 'maravillosas/contacto.html')

def accesorios(request):
    return render(request, 'maravillosas/accesorios.html')

def login(request):
    return render(request, 'maravillosas/login.html')

def registro(request):
    return render(request, 'maravillosas/registro.html')
