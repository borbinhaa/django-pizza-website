# Generated by Django 3.2.7 on 2021-09-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_finalizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempedido',
            name='tamanho',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
