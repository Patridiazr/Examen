from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login as auth_login
from .models import Usuario, Producto, Tienda
# Create your views here.


# REDIRECCION A PAGINAS
def index(request):
    return render(request,'index.html')

def listado(request):
    return render(request,'listado.html')

def tiendas(request):
    return render(request,'tiendas.html')

def productos(request):
    return render(request,'productos.html')

def registro(request):
    return render(request,'registro.html')

def ingresar(request):
    return render(request, 'ingresar.html')


# LOGIN

def login_iniciar(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(request,username=username, password=password)
    print(username,password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/";</script>')

def logout_view(request):
    logout(request)
    return redirect('index')


# Usuarios

def crear_U(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    usuario = Usuario(username=username, password=password)
    usu = User(username=username, password=password)
    usuario.save()
    usu.save()
    return redirect('ingresar')


# Tienda
def crear_T(request):
    nombre
    sucursal
    direccion
    ciudad
    
# Producto