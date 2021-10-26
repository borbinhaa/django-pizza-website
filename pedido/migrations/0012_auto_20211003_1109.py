# Generated by Django 3.2.7 on 2021-10-03 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0011_alter_pedido_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 3, 11, 9, 15, 279236)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='endereco',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('P', 'Pronto'), ('F', 'Finalizado')], default='P', max_length=2),
        ),
    ]
