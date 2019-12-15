from django.db import models


class Empresa(models.Model):
    TIPO_DE_ENDERECO_CHOICES = [
        ('RES', 'RESIDENCIAL'),
        ('COM', 'COMÉRCIAL'),
        ('URB', 'URBANO'),
        ('RUR', 'RURAL')
    ]

    AREA_DE_ATUACAO_CHOICES = [
        ('IND', 'INDÚSTRIA'),
        ('COM', 'COMÉRCIO'),
        ('SER', 'SERVIÇOS'),
        ('ALI', 'ALIMENTAÇÃO'),
        ('SPO', 'ESPORTES'),
        ('TIC', 'TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO')
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

    razao_social = models.CharField(max_length=500)
    cnpj = models.CharField(max_length=20)
    tipo_de_endereco = models.CharField(max_length=3, choices=TIPO_DE_ENDERECO_CHOICES, blank=True, null=False)
    endereco = models.CharField(max_length=60)
    #logradouro = models.CharField(max_length=60)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=30)
    cep = models.CharField(max_length=20)
    uf = models.CharField(max_length=3, choices=UF_CHOICES,blank=False,null=False, default=0)
    telefones = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    site = models.CharField(max_length=60)
    area_de_atuacao = models.CharField(max_length=3, choices=AREA_DE_ATUACAO_CHOICES, blank=True, null=False)


    def __str__(self):
        return self.razao_social

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'