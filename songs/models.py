from django.db import models
from django.contrib.auth.models import User

#escolhas em campos
ESTILOS = (
       ('agitado','agitado'),
       ('adoracao','adoração'),
       ('agitado_adoracao','agitado/adoracao'),
)

RITMO = (
       ('outro','outro'),
       ('axe','axé'),
       ('eletronica','eletronica'),
       ('forro','forró'),
       ('pop','pop'),
       ('rock','rock'),
       ('samba','samba/pagode'),
       ('sertanejo','sertanejo'),
)

# Create your models here.
class Banda(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Bandas'

class Louvor(models.Model):
    """ tem um counter simples de ensaiado/tocado
    tem o tom (esse é um txt simples)
    tem um campo de observações simples"""

    nome = models.CharField(max_length=50)
    numero_da_pasta = models.CharField(max_length=10,blank=True,default='sem numero')
    estilo = models.CharField(max_length=20,choices=ESTILOS,default=ESTILOS[0][0])
    ritmo = models.CharField(max_length=20,choices=RITMO,default=RITMO[0][0])
    vezes_tocada = models.IntegerField(default=0)
    vezes_ensaiada = models.IntegerField(default=0)
    tom = models.CharField(max_length=10,blank=True,default='Original')
    link_cifra = models.URLField(max_length=300)
    favoritado_usuario = models.ManyToManyField(User,blank=True) #usando o próprio modelo padrão de usuário
    banda = models.ManyToManyField(Banda,blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Louvores'