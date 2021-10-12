from django.conf import settings
import os
from PIL import Image
from django.db import models

# Create your models here.


class Sabor(models.Model):
    nome_sabor = models.CharField(
        max_length=100, unique=True, verbose_name='nome do sabor')
    descricao_sabor = models.CharField(
        max_length=100, verbose_name='descrição')
    preco_grande = models.FloatField()
    preco_medio = models.FloatField()
    preco_pequeno = models.FloatField()
    imagem = models.ImageField(upload_to='sabores/', blank=True, null=True)
    no_cardapio = models.BooleanField(
        default=True, verbose_name='Está no cardápio?')
    doce = models.BooleanField(default=False)
    salgado = models.BooleanField(default=False)

    @staticmethod
    def resize_img(img, new_width=800.0):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_img(self.imagem, max_image_size)

    def __str__(self):
        return self.nome_sabor

    class Meta:
        verbose_name = 'Sabor'
        verbose_name_plural = 'Sabores'
