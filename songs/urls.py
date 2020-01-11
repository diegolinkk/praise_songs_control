from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'), #exibe lista geral
    path('agitados/',views.agitados,name='agitados'), #exibe louvores agitados
    path('adoracao/',views.adoracao,name='adoracao'), #exibe louvores de adoração
    path('bandas/',views.bandas,name='bandas'), #exibe lista de bandas
    path('bandas/<int:id_banda>/',views.banda_musicas,name='banda_musicas'), #exibe músicas de uma determinada banda
    path('bandas/cadastro',views.banda_cadastro,name='banda_cadastro'), # cadastro de novas bandas
    path('ensaio/',views.ensaio,name='ensaio'), #exibe controle de ensaio/tocado
    path('ensaiar/<int:id_louvor>/',views.ensaiar,name='ensaiar'), #grava +1 ensaio
    path('tocar/<int:id_louvor>/',views.tocar,name='tocar'), #grava +1 tocado
    path('louvor/<int:id_louvor>/',views.louvor,name='louvor'), #exibe detalhes do louvor + permite edição
    path('louvor/cadastro',views.louvor_cadastro,name='louvor_cadastro') # cadastro de novos louvors
]
