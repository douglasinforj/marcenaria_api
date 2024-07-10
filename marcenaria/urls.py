
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gerenciamento.api.viewsets import FornecedorViewSet, ClienteViewSet, EstoqueViewSet, ProdutoViewSet, PedidoViewSet, PedidoMaterialViewSet, FuncionarioViewSet

router = DefaultRouter()
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'estoque', EstoqueViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'pedido-material', PedidoMaterialViewSet)
router.register(r'funcionarios', FuncionarioViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
