# Generated by Django 3.2.7 on 2021-09-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sabores', '0004_auto_20210907_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabor',
            name='doce',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sabor',
            name='salgado',
            field=models.BooleanField(default=False),
        ),
    ]
