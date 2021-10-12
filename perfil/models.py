from django.core.exceptions import ValidationError
from utils.validacpf import valida_cpf
from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idade = models.PositiveIntegerField()
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    def clean(self) -> None:
        error_msg = {}

        if not valida_cpf(self.cpf):
            error_msg['cpf'] = 'CPF invalido'

        if self.idade:
            if self.idade < 18 or self.idade > 120:
                error_msg['idade'] = 'Idade Inválida'

        if error_msg:
            raise ValidationError(error_msg)


class Endereco(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    rua = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    numero = models.CharField(max_length=5)
    estado = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.rua}, n {self.numero}, {self.cidade}'
