# Generated by Django 3.0 on 2019-12-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0012_auto_20191215_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia_profissional',
            name='forma_de_contratacao',
            field=models.CharField(blank=True, choices=[('T', 'CLT'), ('T', 'TEMPORARIO'), ('C', 'CONTRATO POR EMPREITADA'), ('O', 'OUTRA')], max_length=1, verbose_name='Forma de Contratação'),
        ),
    ]