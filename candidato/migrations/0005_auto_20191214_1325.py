# Generated by Django 3.0 on 2019-12-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0004_candidato_vagas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='data_de_nascimento',
            field=models.DateField(max_length=20),
        ),
    ]
