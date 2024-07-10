from rest_framework import serializers
from ..models import Fornecedor,  Cliente, PedidoMaterial, Pedido, Estoque, Produto

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoMaterial
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    material_usado = PedidoMaterialSerializer(many=True, read_oly=True) #campo Estrangeiro la no models, precisamos serializar

    class Meta:
        model = Pedido
        fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields  = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'