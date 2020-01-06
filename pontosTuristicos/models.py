from django.db import models
from atracoes.models import Atracao
from comentario.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Localizacao

class PontoTuristico (models.Model):
    nome = models.CharField (max_length=150)
    decricao = models.TextField ()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pontos_turisticos_img', null=True, blank=True)

    def __str__ (self):
        return self.nome


