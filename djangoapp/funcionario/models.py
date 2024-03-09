from django.db import models


class Cargo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    
    def __str__(self) -> str:
        return f'Cargo:{self.nome}'

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'Funcionario: {self.nome}'

