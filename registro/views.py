from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login as auth_login
from .models import Usuario, Producto, Tienda, Lista
# Create your views here.


#import de api 

from rest_framework import viewsets
from .serializer import UsuarioSerializer, TiendaSerializer, ProductoSerializer, ListaSerializer

# REDIRECCION A PAGINAS
def index(request):
    listas = Tienda.objects.all()    
    contexto = {'listas': listas}
    return render(request,'index.html',contexto)

def listado(request):
    listas = Lista.objects.all()
    productos = Producto.objects.all()
    contexto = {'listas': listas, 'productos': productos}
    return render(request,'listado.html',contexto)

def tiendas(request):
    tiendas = Tienda.objects.all()
    contexto = {'tiendas': tiendas}
    return render(request,'tiendas.html', contexto)

def productos(request):
    listas = Lista.objects.all()
    tiendas = Tienda.objects.all()
    contexto = {'listas': listas,'tiendas': tiendas}
    return render(request,'productos.html',contexto)

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

def aprobar_T(request,id):
    ti = Tienda.objects.get(id = id)
    ti.aprobado = True
    ti.save()
    return redirect('listado')


def eliminar_T(request,id):
    ti = Tienda.objects.get(id = id)
    ti.delete()
    return redirect('tiendas')

class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer



# Producto
def create_P(request):
    nombre = request.POST.get('nombre','')
    costoP = request.POST.get('costoP','')
    costoR = request.POST.get('costoR','')
    tienda = request.POST.get('tienda','')
    notas = request.POST.get('notas','')
    nlista = request.POST.get('lista','')
    po = Producto(nombre=nombre,costoP=costoP,costoR=costoR,tienda=tienda,notas=notas,nlista=nlista)
    po.save()
    return redirect('listado')

def editar_P(request,id):
    nombre = request.POST.get('nombre')
    costoP = request.POST.get('costoP')
    costoR = request.POST.get('costoR')
    tienda = request.POST.get('tienda')
    notas = request.POST.get('notas')
    po = Producto.objects.get(pk = id)
    po.nombre = nombre
    po.costoP = costoP
    po.costoR = costoR
    po.tienda = tienda
    po.notas = notas
    po.save()
    return redirect('listado')

def eliminar_P(request,id):
    po = Producto.objects.get(pk=id)
    po.remove()
    return redirect('index')

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#Listas

def crear_L(request):
    nombre = request.POST.get('nombre')
    total_A = request.POST.get('')
    total_C = request.POST.get('')
    costo_P = request.POST.get('')
    costo_R = request.POST.get('')
    username = User.username
    list = Lista(nombre=nombre,total_A=total_A,total_C=total_C,costo_P=costo_P,
                costo_R=costo_R,username=username)
    list.save()
    return redirect('listado')

class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer