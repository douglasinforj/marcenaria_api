from rest_framework import serializers
from ..models import Funcionario,Fornecedor,  Cliente, PedidoMaterial, Pedido, Estoque, Produto
from django.contrib.auth.models import User  #usuários do django


#Lidando o campo user:

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Inclua outros campos conforme necessário

class FuncionarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Funcionario
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        funcionario = Funcionario.objects.create(user=user, **validated_data)
        return funcionario

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.nome_completo = validated_data.get('nome_completo', instance.nome_completo)
        instance.save()

        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.save()

        return instance



#Regra de Negocios

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoMaterialSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer(read_only=True)                      #campos que vem de relaciomanetos
    
    class Meta:
        model = PedidoMaterial
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    pedido_material = PedidoMaterialSerializer(many=True, read_only=True)    #campos que vem de relaciomanetos
    funcionario = FuncionarioSerializer(read_only=True)                      #campos que vem de relaciomanetos

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



