from  rest_framework.viewsets import ModelViewSet
from  pontosTuristicos.models import PontoTuristico
from .serializers import PontosTuristicosSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class PontoTuristicoViewSets (ModelViewSet):

    queryset = PontoTuristico.objects.all()
    serializer_class = PontosTuristicosSerializer  # import do arq serializers

    
