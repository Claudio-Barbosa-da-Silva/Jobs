from django.contrib import admin
from .models import Vagas

class VagasInline(admin.TabularInline):
    model = Vagas
    extra = 1

class VagasAdmin(admin.ModelAdmin):
    #Campos pesquisáveis no Admin
    search_fields = ('cargo', 'remuneracao', 'uf', 'empresa')
    list_filter = ('cargo', 'remuneracao', 'uf', 'empresa')
    #Campos que serão visiveis no Admin
    list_display = ('cargo', 'remuneracao', 'uf', 'empresa')
    inline = []

admin.site.register(Vagas, VagasAdmin)