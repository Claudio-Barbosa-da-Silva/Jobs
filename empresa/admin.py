from django.contrib import admin
from vagas.models import Vagas
from .models import Empresa

class VagasInline(admin.TabularInline):
    model = Vagas
    extra = 1

class EmpresaAdmin(admin.ModelAdmin):
    # Campos pesquisáveis no Admin
    search_fields = ('razao_social', 'cnpj', 'area_de_atuacao', 'cidade')
    list_filter = ('razao_social', 'cnpj', 'area_de_atuacao', 'cidade')
    # Campos que serão visiveis no Admin
    list_display = ['razao_social', 'cnpj', 'area_de_atuacao', 'cidade']
    inline = []

admin.site.register(Empresa, EmpresaAdmin)


