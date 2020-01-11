from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('agitados/',views.agitados,name='agitados'),
    path('adoracao/',views.adoracao,name='adoracao'),
    path('bandas/',views.bandas,name='bandas'),
    path('bandas/<int:id_banda>/',views.banda_musicas,name='banda_musicas'),
    path('ensaio/',views.ensaio,name='ensaio'),
    path('ensaiar/<int:id_louvor>/',views.ensaiar,name='ensaiar'),
    path('tocar/<int:id_louvor>/',views.tocar,name='tocar'),
]
