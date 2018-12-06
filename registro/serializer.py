from rest_framework import serializers
from .models import Usuario, Tienda, Producto, Lista


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url','username','password') 

class TiendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tienda
        fields = ('url','nombre','sucursal','direccion','ciudad','region','aprobado') 

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url','nombre','costoP','costoR','tienda','notas','nlista')

class ListaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lista
        fields = ('url','total_A','total_C','costo_P','costo_R','username')