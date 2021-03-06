# Generated by Django 3.0 on 2019-12-12 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20191212_1427'),
        ('vagas', '0005_auto_20191209_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('especificacoes_do_cargo', models.TextField(blank=True)),
                ('remuneracao', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('vale_transporte', models.CharField(choices=[('S', 'SIM'), ('N', 'NAO')], default=0, max_length=1)),
                ('vale_refeicao', models.CharField(choices=[('S', 'SIM'), ('N', 'NAO')], default=0, max_length=1)),
                ('outros', models.TextField(blank=True)),
                ('turno', models.CharField(choices=[('C', 'COMERCIAL'), ('M', 'MATUTINO'), ('V', 'VESPERTINO'), ('N', 'NOTURNO')], default=0, max_length=1)),
                ('forma_de_contratacao', models.CharField(blank=True, choices=[('T', 'CLT'), ('T', 'TEMPORARIO'), ('C', 'CONTRATO POR EMPREITADA')], max_length=1)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default=0, max_length=3)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
    ]
