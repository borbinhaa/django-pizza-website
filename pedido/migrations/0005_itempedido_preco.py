# Generated by Django 3.2.7 on 2021-09-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_itempedido_tamanho'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempedido',
            name='preco',
            field=models.FloatField(null=True),
        ),
    ]