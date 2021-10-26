# Generated by Django 3.2.7 on 2021-09-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sabores', '0003_alter_sabor_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sabor',
            name='descricao_sabor',
            field=models.CharField(max_length=100, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='sabor',
            name='no_cardapio',
            field=models.BooleanField(default=True, verbose_name='Está no cardápio?'),
        ),
        migrations.AlterField(
            model_name='sabor',
            name='nome_sabor',
            field=models.CharField(max_length=100, verbose_name='nome do sabor'),
        ),
    ]