from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Louvor,Banda

# Create your views here.
def index(request):
    louvores = Louvor.objects.all()
    context = {
        "louvores": louvores,
    }
    return render(request,'songs/song_list.html',context=context)

def agitados(request):
    louvores = Louvor.objects.filter(estilo='agitado')
    context = {
    "louvores": louvores,
    }
    return render(request,'songs/song_list.html',context=context)

def adoracao(request):
    louvores = Louvor.objects.filter(estilo='adoracao')
    context = {
    "louvores": louvores,
    }
    return render(request,'songs/song_list.html',context=context)

def bandas(request):
    bandas = Banda.objects.all().order_by('nome')
    context = {
        "bandas": bandas,
    }
    return render(request,'songs/bands.html',context=context)

def banda_musicas(request,id_banda):
    banda = Banda.objects.get(id=id_banda)
    louvores = banda.louvor_set.all
    context = {
        "louvores": louvores,
    }
    return render(request,'songs/song_list.html',context=context)

def ensaio(request):
    louvores = Louvor.objects.all().order_by('vezes_tocada','vezes_ensaiada')
    context = {
        "louvores": louvores,
    }
    return render(request,'songs/song_register.html',context=context)

def ensaiar(request,id_louvor):
    louvor = Louvor.objects.get(id=id_louvor)
    louvor.vezes_ensaiada +=1
    louvor.save()
    return HttpResponseRedirect(reverse('ensaio'))


def tocar(request,id_louvor):
    louvor = Louvor.objects.get(id=id_louvor)
    louvor.vezes_tocada +=1
    louvor.save()
    return HttpResponseRedirect(reverse('ensaio'))