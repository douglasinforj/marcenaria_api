from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .choices import UF_CHOICES, UN_MEDIDA_CHOICES, STATUS_PRODUCAO, CARGOS, SETOR
from django.contrib.auth.models import User


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    sobre_nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    cargo = models.CharField(max_length=20, choices=CARGOS, default='')
    setor = models.CharField(max_length=255, choices=SETOR, default='')
    documentos_upload = models.FileField(upload_to='documentos_funcionarios/', null=True, blank=True)
    fotos_funcionarios = models.ImageField(upload_to='fotos_funcionarios/', null=True, blank=True)

    def __str__(self):
        return f"Funcionario: {self.nome} {self.sobre_nome} | User: {self.user}"



class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj_cpf = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2, choices=UF_CHOICES, default='RJ')
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    vendedor = models.CharField(max_length=255)
    vendedor_telefone = models.CharField(max_length=15)
    documentos_upload = models.FileField(upload_to='documentos_fornecedor/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cnpj_cpf = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2, choices=UF_CHOICES, default='RJ')
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    vendedor = models.CharField(max_length=255)
    documentos_upload = models.FileField(upload_to='documentos_cliente/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    codigo_produto = models.CharField(max_length=100)
    descricao_produto = models.TextField()
    fotos_produto = models.ImageField(upload_to='fotos_produto/', null=True, blank=True)
    documentos_upload = models.FileField(upload_to='documentos_produto/', null=True, blank=True)

    def __str__(self):
        return self.nome_produto

class Estoque(models.Model):
    nome_material = models.CharField(max_length=255)
    largura = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    altura = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comprimento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    un_medida = models.CharField(max_length=7, choices=UN_MEDIDA_CHOICES, default='')
    preco_comprado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantidade_estoque = models.IntegerField()
    validade = models.DateField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    documentos_upload = models.FileField(upload_to='documentos/', null=True, blank=True)
    fotos_produtos = models.ImageField(upload_to='fotos_produtos/', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome_material

class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_PRODUCAO, default='')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido de {self.produto.nome_produto} para {self.cliente.nome}"

class PedidoMaterial(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='pedido_material', on_delete=models.CASCADE)
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    quantidade_utilizada = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade_utilizada} de {self.estoque.nome_material} no Pedido {self.pedido.id}"

@receiver(post_save, sender=PedidoMaterial)
def update_stock(sender, instance, **kwargs):
    material = instance.estoque
    material.quantidade_estoque -= instance.quantidade_utilizada
    material.save()
