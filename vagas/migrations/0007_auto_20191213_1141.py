# Generated by Django 3.0 on 2019-12-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0006_auto_20191212_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='remuneracao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
        ),
    ]