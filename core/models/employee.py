from django.db import models

class Funcionario(models.Model):
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=80)
    horas_trabalhadas = models.IntegerField()
    telefone_funcionario = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
