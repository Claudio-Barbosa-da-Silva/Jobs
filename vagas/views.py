from django.shortcuts import render, redirect
from .models import Vagas
#from .form import VagasForm
import datetime
# Create your views here.

def index(request):
    date = {}
    date['new'] = datetime.datetime.now()

    date ['menu'] = ['Contato', 'Vagas', 'Empresa', 'Candidatos']
    return render(request, 'vagas/index.html', date)

def listagem(request):
    data = {}
    data['vaga'] = Vagas.objects.all()
    return render(request, 'vagas/listagem.html', data)

def cria_vagas(request):
    data = {}
    form = VagasForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect ('url_listagem')

    data ['form'] = form
    return render(request, 'vagas/form.html', data )
