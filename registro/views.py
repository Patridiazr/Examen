from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login as auth_login
from .models import Usuario, Producto, Tienda
# Create your views here.


#import de api 

from rest_framework import viewsets
from .serializer import UsuarioSerializer

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

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Tienda
def crear_T(request):
    nombre = request.POST.get('nombre')
    sucursal = request.POST.get('sucursal')
    direccion = request.POST.get('direccion')
    ciudad = request.POST.get('ciudad')
    region = request.POST.get('region')
    ti = Tienda(nombre=nombre, sucursal=sucursal, direccion=direccion, ciudad=ciudad, region=region)
    ti.save()
    return redirect('tiendas')

def aprovar_T(request,id):
    ti = Tienda.objects.all(pk = id)
    ti.aprobado = True
    ti.save()
    return redirect('listado')

def eliminar_T(request,id):
    ti = Tienda.objects.all(pk = id)
    ti.remove()
    return redirect('tiendas')



# Producto
def create_P(request):
    nombre = request.POST.get('nombre','')
    costoP = request.POST.get('costoP','')
    costoR = request.POST.get('costoR','')
    tienda = request.POST.get('tienda','')
    notas = request.POST.get('notas','')
    po = Producto(nombre=nombre,costoP=costoP,costoR=costoR,tienda=tienda,notas=notas)
    po.save()
    return redirect('index')
    
def editar_P(request,id):
    nombre = request.POST.get('nombre')
    costoP = request.POST.get('costoP')
    costoR = request.POST.get('costoR')
    tienda = request.POST.get('tienda')
    notas = request.POST.get('notas')
    po = Producto.objects.all(pk = id)
    po.nombre = nombre
    po.costoP = costoP
    po.costoR = costoR
    po.tienda = tienda
    po.notas = notas
    po.save()
    return redirect('index')

def eliminar_P(request,id):
    po = Producto.objects.all(pk=id)
    po.remove()
    return redirect('index')
