from rest_framework import serializers
from .models import Colaborador, Rol, User, TipoIngrediente, Ingrediente, EstadoPedido, Pedido, DetallePedido
from django.contrib.auth.models import User

class AuthHySerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name']


class RolHySerializers(serializers.ModelSerializer):
    #colaborador = ColaboradorHySerializers(many=True, read_only=False)
    class Meta:
        model = Rol
        fields = ['id','roles']

class ColaboradorHySerializers(serializers.ModelSerializer):
    user = AuthHySerializers()
    roles = RolHySerializers()
    class Meta:
        model = Colaborador
        fields = ['id','user','Localidad','edad','roles']

#MAGALY
    
class IngredienteHySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'
        #fields = ['id','ingrediente','precio','cantidad','imagen']

class TipoIngredienteHySerializer(serializers.ModelSerializer):
    ingrediente = IngredienteHySerializer(many=True, read_only=False)
    class Meta:
        model = TipoIngrediente
        fields = ['id','nombre','ingrediente']

class EstadoPedidoHySerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = ['id','estado']

class DetallePedidoHySerializer(serializers.ModelSerializer):
    ingrediente = IngredienteHySerializer()
    class Meta:
        model = DetallePedido
        fields = ['id','ingrediente','cantidad','precio']
    
    '''   
    def create(self, validate_data):
        return Pedido.objects.create(**validate_data)
    '''   
class PedidoHySerializer(serializers.ModelSerializer):
    estado = EstadoPedidoHySerializer()
    detallepedido = DetallePedidoHySerializer(many=True, read_only=False)
    class Meta:
        model = Pedido
        fields = ['id','cliente','detallepedido','fecha_pedido','monto_total','estado','atendidopor']
    
    '''    
    def create(self, validate_data):
        return Pedido.objects.create(**validate_data)
        '''