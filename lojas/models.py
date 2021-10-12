from django.db import models
from django.forms import ValidationError
import re


class Lojas(models.Model):
    estado = models.CharField(
        max_length=2,
        choices=(
            ('SP', 'São Paulo'),
            ('SC', 'Santa Catarina'),
            ('RJ', 'RJ'),
        )
    )
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    celular = models.CharField(max_length=11)

    def __str__(self) -> str:
        return f'{self.estado}, {self.rua}'

    def clean(self) -> None:
        error_msg = {}

        if re.search(r'[^0-9]', self.celular) or len(self.celular) != 11:
            error_msg['celular'] = 'Digite apenas números, precisa ter 11'\
                ' carácteres'

        if error_msg:
            raise ValidationError(error_msg)

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
