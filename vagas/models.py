from django.db import models

# Create your models here.

class Cargo(models.Model):
    VALE_TRANSPORTE_CHOICES = [
        ("S", 'SIM'),
        ("N", 'NAO'),
    ]

    VALE_REFEICAO_CHOICES = [
        ("S", 'SIM'),
        ("N", 'NAO'),
    ]

    TURNO_CHOICES = [
        ('C', 'COMERCIAL'),
        ('M', 'MATUTINO'),
        ('V', 'VESPERTINO'),
        ('N', 'NOTURNO'),
    ]

    FORMA_DE_CONTRATACAO_CHOICES = [
        ("T", 'CLT'),
        ("T", 'TEMPORARIO'),
        ('C', 'CONTRATO POR EMPREITADA'),
    ]

    UF_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    nome = models.CharField(max_length=500)
    especificacoes_do_cargo = models.TextField(blank = True)
    remuneracao = models.DecimalField(max_digits=19, decimal_places=10, default=0)
    vale_transporte = models.CharField(max_length=1, choices =VALE_TRANSPORTE_CHOICES, blank=False, null=False, default=0)
    vale_refeicao = models.CharField(max_length=1, choices= VALE_REFEICAO_CHOICES, blank=False, null=False, default=0)
    outros = models.TextField(blank = True)
    turno = models.CharField(max_length=1, choices= TURNO_CHOICES,blank=False,null=False, default=0)
    forma_de_contratacao = models.CharField(max_length=1, choices=FORMA_DE_CONTRATACAO_CHOICES, blank=True, null=False)
    uf = models.CharField(max_length=3, choices=UF_CHOICES,blank=False,null=False, default=0)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Cargo'


