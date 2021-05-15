from django.db import models
from django.conf import settings
from django.utils import timezone

class Ministerio(models.Model):

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    orcamento = models.FloatField()
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nome