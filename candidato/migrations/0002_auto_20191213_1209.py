# Generated by Django 3.0 on 2019-12-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='telefones',
        ),
        migrations.AddField(
            model_name='candidato',
            name='celular',
            field=models.CharField(blank=True, max_length=20, verbose_name='celular'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, verbose_name='telefone'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='uf_da_expedicao',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default=0, max_length=3),
        ),
    ]
