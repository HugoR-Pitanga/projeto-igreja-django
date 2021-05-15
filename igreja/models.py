from django.db import models
from django.conf import settings
from django.db.models.fields import CharField
from django.utils import timezone

class Ministerio(models.Model):

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    orcamento = models.FloatField()
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nome

class Agenda(models.Model):
    nome = models.CharField(max_length=300)
    data = models.DateField()

    def __str__(self):
        return self.nome

class OrigemMovimentoFinanceiro(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class TipoMovimentoFinanceiro(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class MovimentoFinanceiro(models.Model):
    tipo = models.ForeignKey(TipoMovimentoFinanceiro, on_delete=models.CASCADE)
    origem = models.ForeignKey(OrigemMovimentoFinanceiro, on_delete=models.CASCADE)
    data_movimento = models.DateField()
    valor = models.FloatField(default=0.0)

    def __str__(self):
        return self.data_movimento