# Generated by Django 3.0 on 2019-12-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0010_auto_20191214_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='cargo',
            field=models.CharField(max_length=500, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='especificacoes_do_cargo',
            field=models.TextField(blank=True, verbose_name='Especificações do Cargo'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='forma_de_contratacao',
            field=models.CharField(blank=True, choices=[('T', 'CLT'), ('T', 'TEMPORARIO'), ('C', 'CONTRATO POR EMPREITADA')], max_length=1, verbose_name='Forma de Contratação'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='outros',
            field=models.TextField(blank=True, verbose_name='Outras Informações'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='remuneracao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Remuneração'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='turno',
            field=models.CharField(choices=[('C', 'COMERCIAL'), ('M', 'MATUTINO'), ('V', 'VESPERTINO'), ('N', 'NOTURNO')], default=0, max_length=1, verbose_name='Turno'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='uf',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default=0, max_length=3, verbose_name='UF'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='vale_refeicao',
            field=models.CharField(choices=[('S', 'SIM'), ('N', 'NAO')], default=0, max_length=1, verbose_name='Vale Refeição'),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='vale_transporte',
            field=models.CharField(choices=[('S', 'SIM'), ('N', 'NAO')], default=0, max_length=1, verbose_name='Vale Transporte'),
        ),
    ]
