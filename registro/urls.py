from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login 
from django.contrib.auth.decorators import login_required

urlpatterns =[
    path('', views.index, name="index"),
    path('registro/', views.registro, name="registro"),
    path('ingresar/', views.ingresar, name="ingresar"),
    path('salir/', views.logout, name="salir")
]