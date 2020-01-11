from django.forms import ModelForm
from .models import Louvor,Banda

class LouvorForm(ModelForm):
    class Meta:
        model = Louvor
        fields = ['nome','numero_da_pasta','estilo','ritmo','vezes_tocada','vezes_ensaiada','tom','link_cifra','observacoes','banda']

class BandaForm(ModelForm):
    class Meta:
        model = Banda
        fields = ['nome']
