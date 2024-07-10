from django.db import models
from .choices import UF_CHOICES


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