from django.shortcuts import render
from django.http import HttpResponse

from fullCycle.models import Aula

# Create your views here.
def index(request):
    context = {  }
    return render(request, 'website/index.html', context)

def listclass(request):
    aulas = Aula.objetos.all()
    context = { 'aulas': aulas }
    return render(request, 'website/list.html', context)