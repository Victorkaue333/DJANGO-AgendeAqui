from django.db import models


class Bloco(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Recurso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.PositiveIntegerField(default=0)
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT, related_name='salas')
    recursos = models.ManyToManyField(Recurso, blank=True, related_name='salas')

    def __str__(self):
        bloco_nome = self.bloco.nome if self.bloco else ''
        return f"{self.nome} ({bloco_nome})"
