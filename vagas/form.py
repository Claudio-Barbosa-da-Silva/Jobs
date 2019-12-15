from django.forms import ModelForm
from .models import Vagas

class VagasForm(ModelForm):
    class Meta:
        model = Vagas
        fields = ['empresa', 'cargo', 'especificacoes_do_cargo', 'remuneracao', 'uf']
