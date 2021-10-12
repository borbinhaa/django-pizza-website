from django.db import models
from perfil.models import Perfil
from datetime import datetime


class Pedido(models.Model):
    perfil_pedido = models.ForeignKey(
        Perfil, on_delete=models.CASCADE, verbose_name='Cliente')
    total = models.FloatField()
    endereco = models.CharField(max_length=255)
    status = models.CharField(
        max_length=2,
        default='P',
        choices=(('P', 'Preparando'), ('E', 'Enviado'), ('R', 'Recebido'))
    )
    data = models.DateTimeField(
        default=datetime.now())

    def __str__(self) -> str:
        return f'Pedido {self.id}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    sabor = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.FloatField()

    def __str__(self) -> str:
        return self.sabor
