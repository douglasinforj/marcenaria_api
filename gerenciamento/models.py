from django.db import models
from .choices import UF_CHOICES, UN_MEDIDA_CHOICES


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
