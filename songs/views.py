from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Louvor,Banda
from .forms import LouvorForm,BandaForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    louvores = Louvor.objects.all()
    context = {
        "louvores": louvores,
    }
    return render(request,'songs/song_list.html',context=context)

@login_required
def agitados(request):
    louvores = Louvor.objects.filter(Q(estilo='agitado_adoracao') | Q(estilo='agitado'))
    context = {
    "louvores": louvores,
    }
    return render(request,'songs/song_list.html',context=context)

@login_required
def adoracao(request):
    louvores = Louvor.objects.filter(Q(estilo='agitado_adoracao') | Q(estilo='adoracao'))
    context = {
    "louvores": louvores,
    }
    return render(request,'songs/song_list.html',context=context)

@login_required
def bandas(request):
    bandas = Banda.objects.all().order_by('nome')
    context = {
        "bandas": bandas,
    }
    return render(request,'songs/bands.html',context=context)

@login_required
def banda_musicas(request,id_banda):
    banda = Banda.objects.get(id=id_banda)
    louvores = banda.louvor_set.all
    context = {
        "louvores": louvores,
    }
    return render(request,'songs/song_list.html',context=context)

@login_required
def banda_cadastro(request):

    if request.method =='POST':
        form = BandaForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))


    form = BandaForm()
    context = {
        'form':form
    }
    return render(request,'songs/band.html',context= context)
    
@login_required
def ensaio(request):
    louvores = Louvor.objects.all().order_by('vezes_tocada')
    context = {
        "louvores": louvores,
    }
    return render(request,'songs/song_register.html',context=context)

@login_required
def ensaiar(request,id_louvor):
    louvor = Louvor.objects.get(id=id_louvor)
    louvor.vezes_ensaiada +=1
    louvor.save()
    return HttpResponseRedirect(reverse('ensaio'))

@login_required
def tocar(request,id_louvor):
    louvor = Louvor.objects.get(id=id_louvor)
    louvor.vezes_tocada +=1
    louvor.save()
    return HttpResponseRedirect(reverse('ensaio'))

@login_required
def louvor(request,id_louvor):
    louvor = Louvor.objects.get(id=id_louvor)

    if request.method == 'POST':
        form = LouvorForm(instance = louvor, data = request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('louvor',args= [id_louvor])) #caso precisar permanecer no form
            return HttpResponseRedirect(reverse('index'))

    form = LouvorForm(instance=louvor)
    #falta regra de salvar em post

    context = {
        'louvor': louvor,
        'form': form,
    }
    return render(request,'songs/louvor.html',context=context)

@login_required
def louvor_cadastro(request):
    form = LouvorForm()

    if request.method == 'POST':
        form = LouvorForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    context = {
        'form':form,
    }
    return render(request,'songs/louvor.html',context=context)