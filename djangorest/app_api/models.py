from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    faixa = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
