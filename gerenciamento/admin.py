from django.contrib import admin
from .models import Fornecedor, Cliente, PedidoMaterial, Pedido, Estoque, Produto, Funcionario

class PedidoMaterialInline(admin.TabularInline):
    model = PedidoMaterial
    extra = 1  # Número de linhas extras para adicionar no inline

# Opcionalmente, você pode usar StackedInline para uma apresentação diferente:
#class PedidoMaterialInline(admin.StackedInline):
   # model = PedidoMaterial
   # extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [PedidoMaterialInline]
    list_display = ['produto', 'cliente', 'status', 'criado_em', 'atualizado_em']
    list_filter = ['status', 'criado_em', 'atualizado_em']
    search_fields = ['produto__nome_produto', 'cliente__nome']


class PedidoAdmin(admin.ModelAdmin):
    inlines = [PedidoMaterialInline]



admin.site.register(Fornecedor)
admin.site.register(Cliente)
admin.site.register(Estoque)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoMaterial)
admin.site.register(Produto)
admin.site.register(Funcionario)
