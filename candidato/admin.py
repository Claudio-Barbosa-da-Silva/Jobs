from django.contrib import admin
from .models import Candidato
from empresa.models import Empresa
from vagas.models import Vagas
from .models import Experiencia_Profissional
# Register your models here.

class EmpresaInline(admin.TabularInline):
    model = Empresa
    extra = 1

class VagasInline(admin.TabularInline):
    model = Vagas
    extra = 1

class CandidatoAdmin(admin.ModelAdmin):
    # Campos pesquisáveis no Admin
    search_fields = ('nome_completo', 'cpf', 'data_de_nascimento', 'estado_civil', 'cidade')
    list_filter = ('nome_completo', 'cpf', 'data_de_nascimento', 'estado_civil', 'cidade')
    # Campos que serão visiveis no Admin
    list_display = ('nome_completo', 'cpf', 'data_de_nascimento', 'estado_civil', 'cidade')
    inline = []

class ExperienciaFuncionalAdmin(admin.ModelAdmin):
    # Campos pesquisáveis no Admin
    search_fields = ('candidato', 'empresa', 'cargo', 'data_de_inicio', 'data_fim')
    list_filter = ('candidato', 'empresa', 'cargo', 'data_de_inicio', 'data_fim')
    # Campos que serão visiveis no Admin
    list_display = ('candidato', 'empresa', 'cargo', 'data_de_inicio', 'data_fim')
    inline = []


admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Experiencia_Profissional, ExperienciaFuncionalAdmin)
