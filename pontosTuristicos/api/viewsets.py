from  rest_framework.viewsets import ModelViewSet
from  pontosTuristicos.models import PontoTuristico
from .serializers import PontosTuristicosSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend #Adicionar no app e tambem chamar REST_FRAMEWORK = {}
class PontoTuristicoViewSets (ModelViewSet):
    queryset = PontoTuristico.objects.all()
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontosTuristicosSerializer  # import do arq serializers
    filterset_fields = ('id', 'nome', 'decricao', 'atracao', )

#Link Tutorial: https://sunscrapers.com/blog/the-ultimate-tutorial-for-django-rest-framework-filtering-part-5/
# Pra passar um parametro na URL coloca --> ?parametro=valor&segundoparametro=valor