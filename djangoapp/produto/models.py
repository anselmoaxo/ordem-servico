from django.db import models
from categoria import Categoria


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)