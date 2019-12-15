from django.db import models
#from model.Vagas import UF_CHOICES

# Create your models here.

class Candidato(models.Model):
    TIPO_DE_ENDERECO_CHOICES = [
        ('RES', 'RESIDENCIAL'),
        ('COM', 'COMÉRCIAL'),
        ('URB', 'URBANO'),
        ('RUR', 'RURAL')
    ]

    ESTADO_CIVIL_CHOICES = [
        ('SOLTEIRO', 'SOLTEIRO'),
        ('CASADO', 'CASADO(A)'),
        ('VIUVO', 'VIÚVO(A)'),
        ('UNIAO ESTAVEL', 'UNIAO ESTÁVEL')

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

    nome_completo = models.CharField('Nome Completo', max_length=500)
    cpf = models.CharField('CPF', max_length=14)
    rg = models.CharField('RG', max_length=30)
    orgao_expedidor = models.CharField('Orgão Expedidor', max_length=30)
    data_de_expedicao = models.DateField('Data de Expedição', max_length=8)
    uf_da_expedicao = models.CharField('UF', max_length=3,  choices=UF_CHOICES, blank=False,null=False, default=0)#choices=UF_CHOICES,
    data_de_nascimento = models.DateField('Data de Nascimento', max_length=20)
    estado_civil = models.CharField('Estado Civil', max_length=30, choices=ESTADO_CIVIL_CHOICES, blank=False,null=False, default=0)
    tipo_de_endereco = models.CharField('Tipo de Endereço', max_length=3, choices=TIPO_DE_ENDERECO_CHOICES, blank=True, null=False)
    endereco = models.CharField('Endereço', max_length=60)
    #logradouro = models.CharField(max_length=60)
    numero = models.CharField('Número', max_length=10)
    bairro = models.CharField('Bairro', max_length=60)
    cidade = models.CharField('Cidade', max_length=30)
    cep = models.CharField('CEP', max_length=8)
    uf = models.CharField('UF', max_length=3, choices=UF_CHOICES,blank=False,null=False, default=0)
    telefone = models.CharField('Telefone',max_length=20, blank=False)
    celular = models.CharField('Celular',max_length=20, blank=True)
    email = models.EmailField('E-mail', max_length=60, blank=True)
    site = models.CharField('Sítio', max_length=60, blank=True)
    vagas = models.ManyToManyField('vagas.vagas')


    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'


class Experiencia_Profissional(models.Model):
    FORMA_DE_CONTRATACAO_CHOICES = [
        ("T", 'CLT'),
        ("T", 'TEMPORARIO'),
        ('C', 'CONTRATO POR EMPREITADA'),
        ('O', 'OUTRA')
    ]

    candidato = models.ForeignKey('candidato.candidato', on_delete=models.CASCADE)
    empresa = models.CharField('Empresa', max_length=150)
    cargo = models.CharField('Cargo', max_length=150)
    tarefas_executadas = models.TextField('Tarefas Executadas',null=False, blank=False)
    forma_de_contratacao = models.CharField('Forma de Contratação', max_length=1, choices=FORMA_DE_CONTRATACAO_CHOICES, blank=True, null=False)
    data_de_inicio = models.DateField('Data de Início', max_length=12)
    data_fim = models.DateField('Data da Saída do Emprego', max_length=12)

    def __str__(self):
        return self.cargo

    class Meta:
        verbose_name = 'Experiência Profissional'
        verbose_name_plural = 'Experiências Profissionais'

