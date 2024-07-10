from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Fornecedor, Cliente, PedidoMaterial, Pedido, Estoque, Produto, Funcionario
from .serializers import (
    FornecedorSerializer, ClienteSerializer, PedidoMaterialSerializer,
    PedidoSerializer, EstoqueSerializer, ProdutoSerializer, FuncionarioSerializer
)
from rest_framework.permissions import IsAuthenticated



class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoMaterialViewSet(viewsets.ModelViewSet):
    queryset = PedidoMaterial.objects.all()
    serializer_class = PedidoMaterialSerializer
    permission_classes = [IsAuthenticated]
     
    #salvar como usuário autenticado
    def perform_create(self, serializer):
        funcionario = Funcionario.objects.get(user=self.request.user)
        serializer.save(funcionario=funcionario)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        instance = serializer.save()
        material = instance.estoque
        material.quantidade_estoque -= instance.quantidade_utilizada
        material.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        instance = serializer.save()
        material = instance.estoque
        material.quantidade_estoque -= instance.quantidade_utilizada
        material.save()

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        funcionario = Funcionario.objects.get(user=self.request.user)
        serializer.save(funcionario=funcionario)




class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
