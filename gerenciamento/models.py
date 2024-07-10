from django.db import models
from .choices import UF_CHOICES, UN_MEDIDA_CHOICES, STATUS_PRODUCAO


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

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    codigo_produto = models.CharField(max_length=100)
    descricao_produto = models.TextField()


class Estoque(models.Model):
    nome_material = models.CharField(max_length=255)
    largura = models.DecimalField(max_digits=10, decimal_places=2)
    altura = models.DecimalField(max_digits=10, decimal_places=2)
    comprimento = models.DecimalField(max_digits=10, decimal_places=2)
    un_medida =  models.CharField(max_length=7 ,choices=UN_MEDIDA_CHOICES, default='')
    preco_comprado = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    validade = models.DateField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    documentos_upload = models.FileField(upload_to='documentos/')
    fotos_produtos = models.ImageField(upload_to='fotos_produtos/')
    descricao = models.TextField()

class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    material_usado = models.ManyToManyField(Estoque, through='PedidoMaterial')
    cliente = models.ForeignKey(Cliente, on_delete=models)
    status = models.CharField(max_length=20 ,choices=STATUS_PRODUCAO, default='')
    criado_em = models.DateTimeField(auto_now_add =True)
    atualizado_em = models.DateTimeField(auto_now =True)

class PedidoMaterial(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    quantidade_utilizada = models.DecimalField(max_digits=10, decimal_places=2)
    preco = models.DecimalField(max_digits=10, decimal_places=2)