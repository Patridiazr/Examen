from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login 
from django.contrib.auth.decorators import login_required
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'usuario',views.UsuarioViewSet)


urlpatterns =[
    path('home/',views.index, name="index"),
    path('listado/',views.listado, name="listado"),
    path('tiendas/',views.tiendas, name="tiendas"),
    path('tiendas/crear_T',views.crear_T, name="crear_T"),
    path('productos/',views.productos, name="productos"),
    path('productos/crear_p',views.create_P, name="crear_p"),
    path('registro/',views.registro, name="registro"),
    path('',views.ingresar, name="ingresar"),
    path('login/',views.login_iniciar, name="login"),
    path('salir/',views.logout_view, name="salir"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api/', include(router.urls)),
]