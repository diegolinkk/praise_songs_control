from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bandas/',views.bandas,name='bandas'),
    path('bandas/<int:id_banda>/',views.banda_musicas,name='banda_musicas'),
]
