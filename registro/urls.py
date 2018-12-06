from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login 
from django.contrib.auth.decorators import login_required

urlpatterns =[
    path('home/',views.index, name="index"),
    path('listado/',views.listado, name="listado"),
    path('tiendas/',views.tiendas, name="tiendas"),
    path('prductos/',views.productos, name="productos"),
    path('registro/',views.registro, name="registro"),
    path('',views.ingresar, name="ingresar"),
    path('salir/',views.logout, name="salir"),
    path('oauth/', include('social_django.urls', namespace='social')),
]