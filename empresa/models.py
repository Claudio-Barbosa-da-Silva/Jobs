from django.db import models

# Create your models here.

class Cadastrar(models.Model):
    TIPO_DE_ENDEREÇO_CHOICES = [
        ('RES', 'RESIDENCIAL'),
        ('COM', 'COMÉRCIAL'),
        ('URB', 'URBANO'),
        ('RUR', 'RURAL'),

    ]

    AREA_DE_ATUACAO_CHOICES = [
        ('IND', 'INDÚSTRIA'),
        ('COM', 'COMÉRCIO'),
        ('SER', 'SERVIÇOS'),
        ('ALI', 'ALIMENTAÇÃO'),
        ('SPO', 'ESPORTES'),
        ('TIC', 'TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO'),

    ]

    Razão_Social = models.CharField(max_length=500)
    CNPJ = models.CharField(max_length=14)
    Tipo_de_Endereço = models.CharField(max_length=3, choices=TIPO_DE_ENDEREÇO_CHOICES, blank=True, null=False)
    Endereço = models.CharField(max_length=60)
    logradouro = models.CharField(max_length=60)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=30, )
    cep = models.CharField(max_length=8)
    uf = models.CharField(max_length=30)#on_delete=models.CASCADE)
    telefones = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    site = models.CharField(max_length=60)
    Área_de_Atuação = models.CharField(max_length=3, choices=AREA_DE_ATUACAO_CHOICES, blank=True, null=False)


    def __str__(self):
        return self.Razão_Social

    class Meta:
        verbose_name_plural = 'Cadastrar'