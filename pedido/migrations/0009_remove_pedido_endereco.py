# Generated by Django 3.2.7 on 2021-09-30 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0008_pedido_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='endereco',
        ),
    ]