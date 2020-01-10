from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Louvor,Banda

# Create your views here.
def index(request):
    louvores = Louvor.objects.all()
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
