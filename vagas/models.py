from django.db import models


# Create your models here.

class Vagas(models.Model):
    VALE_TRANSPORTE_CHOICES = [
        ("S", 'SIM'),
        ("N", 'NAO')
    ]

    VALE_REFEICAO_CHOICES = [
        ("S", 'SIM'),
        ("N", 'NAO')
    ]

    TURNO_CHOICES = [
        ('C', 'COMERCIAL'),
        ('M', 'MATUTINO'),
        ('V', 'VESPERTINO'),
        ('N', 'NOTURNO')
    ]

    FORMA_DE_CONTRATACAO_CHOICES = [
        ("T", 'CLT'),
        ("T", 'TEMPORARIO'),
        ('C', 'CONTRATO POR EMPREITADA')
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

    cargo = models.CharField('Cargo', max_length=500, )
    empresa = models.ForeignKey('empresa.empresa', on_delete=models.CASCADE)
    especificacoes_do_cargo = models.TextField('Especificações do Cargo', blank = True)
    remuneracao = models.DecimalField('Remuneração', max_digits=19, decimal_places=2, default=0)
    vale_transporte = models.CharField('Vale Transporte', max_length=1, choices =VALE_TRANSPORTE_CHOICES, blank=False, null=False, default=0)
    vale_refeicao = models.CharField('Vale Refeição', max_length=1, choices= VALE_REFEICAO_CHOICES, blank=False, null=False, default=0)
    turno = models.CharField('Turno', max_length=1, choices= TURNO_CHOICES,blank=False,null=False, default=0)
    forma_de_contratacao = models.CharField('Forma de Contratação', max_length=1, choices=FORMA_DE_CONTRATACAO_CHOICES, blank=True, null=False)
    #cidade = models.CharField('Cidade', max_length=30, blank=True)
    uf = models.CharField('UF', max_length=3, choices=UF_CHOICES,blank=False,null=False, default=0)
    outros = models.TextField('Outras Informações', blank=True)

    def __str__(self):
        return self.cargo

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'


