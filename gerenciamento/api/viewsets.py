from rest_framework import viewsets
from ..models import Fornecedor,  Cliente, PedidoMaterial, Pedido, Estoque, Produto
from .serializers import FornecedorSerializer, ClienteSerializer, PedidoSerializer, PedidoMaterialSerializer, ProdutoSerializer, EstoqueSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoMateriallViewSet(viewsets.ModelViewSet):
    queryset = PedidoMaterial.objects.all() 
    serializer_class = PedidoMaterialSerializer
