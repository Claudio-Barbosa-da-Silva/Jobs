# Generated by Django 3.0 on 2019-12-15 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0010_auto_20191214_1325'),
        ('candidato', '0007_candidato_vagas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='celular',
            field=models.CharField(blank=True, max_length=20, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='site',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='telefone',
            field=models.CharField(max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='vagas',
            field=models.ManyToManyField(to='vagas.Vagas'),
        ),
    ]
