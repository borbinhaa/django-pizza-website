# Generated by Django 3.2.7 on 2021-09-08 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20210908_1043'),
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='preco_grande',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='preco_medio',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='preco_pequeno',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='quantidade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='sabor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='sabor_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='perfil_pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.perfil'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]