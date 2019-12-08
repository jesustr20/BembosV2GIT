from rest_framework import viewsets, filters, permissions
from .models import Colaborador, User, Rol, TipoIngrediente, Ingrediente, EstadoPedido,Pedido, DetallePedido, User
from django.contrib.auth.models import User
#from .serializers import UsuarioSerializers, AuthSerializers, RolSerializers
from .serializers import RolHySerializers, AuthHySerializers, ColaboradorHySerializers
from .serializers import TipoIngredienteHySerializer, IngredienteHySerializer, EstadoPedidoHySerializer
from .serializers import PedidoHySerializer, DetallePedidoHySerializer, AuthHySerializers

#HyperlinkedModelSerializers
class RolHypViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolHySerializers

class ColaboradorHypViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorHySerializers

#Magaly
class IngredienteHypViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteHySerializer

class TipoIngredienteHypViewSet(viewsets.ModelViewSet):
    queryset = TipoIngrediente.objects.all()
    serializer_class = TipoIngredienteHySerializer

class EstadoPedidoHypViewSet(viewsets.ModelViewSet):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoHySerializer

class PedidoHypViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoHySerializer

class DetallePedidoHypViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoHySerializer