# Generated by Django 3.0 on 2019-12-10 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0004_auto_20191203_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='forma_de_contratacao',
            field=models.CharField(blank=True, choices=[('T', 'CLT'), ('T', 'TEMPORARIO'), ('C', 'CONTRATO POR EMPREITADA')], max_length=1),
        ),
    ]
