# Generated by Django 3.2.7 on 2021-09-07 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sabores', '0002_sabor_no_cardapio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sabor',
            options={'verbose_name': 'Sabor', 'verbose_name_plural': 'Sabores'},
        ),
    ]