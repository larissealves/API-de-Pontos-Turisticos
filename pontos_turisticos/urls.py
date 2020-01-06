from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from pontosTuristicos.api.viewsets import PontoTuristicoViewSets
from atracoes.api.viewsets import AtracoesViewSets
from localizacao.api.viewsets import LocalizacaoViewSets
from avaliacoes.api.viewsets import  AvaliacaoViewSets

router = routers.DefaultRouter()
router.register('pontosTuristicos', PontoTuristicoViewSets, basename = 'PontoTuristico') 
router.register('atracoes', AtracoesViewSets) # EndPoint 
router.register('localizacao', LocalizacaoViewSets) # EndPoint 
router.register('Avaliacao', AvaliacaoViewSets) # EndPoint 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), #rest_framework
    path('', include('comentario.urls')), #rest_framework
]
