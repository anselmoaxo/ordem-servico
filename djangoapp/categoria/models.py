from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    
    def __str__(self) -> str:
        return self.nome