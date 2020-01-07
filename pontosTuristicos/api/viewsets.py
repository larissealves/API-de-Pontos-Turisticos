from  rest_framework.viewsets import ModelViewSet
from  pontosTuristicos.models import PontoTuristico
from .serializers import PontosTuristicosSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters 
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend #Instalar, adicionar no app e tambem chamar REST_FRAMEWORK ={}
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend #Adicionar no app e tambem chamar REST_FRAMEWORK = {}
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class PontoTuristicoViewSets (ModelViewSet):
    queryset = PontoTuristico.objects.all()
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontosTuristicosSerializer  # import do arq serializers
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_fields = ('id', 'nome', 'decricao',  )
    filter_backends = (SearchFilter,)
    search_fields = ('id','nome', 'decricao') # Apresenta todos os resultados que contenham o 'valor' passado pelo usuario
    lookup_field = 'nome'

#Link Tutorial: https://sunscrapers.com/blog/the-ultimate-tutorial-for-django-rest-framework-filtering-part-5/
# Pra passar um parametro na URL coloca --> ?parametro=valor&segundoparametro=valor
#search urls /?search=valor
#look_field: Busca registro pela string, apresenta problema com dados duplicados (Só passar campos unicos)
# Urlnormal/string/

#Link Tutorial: https://sunscrapers.com/blog/the-ultimate-tutorial-for-django-rest-framework-filtering-part-5/
# Pra passar um parametro na URL coloca --> ?parametro=valor&segundoparametro=valor
