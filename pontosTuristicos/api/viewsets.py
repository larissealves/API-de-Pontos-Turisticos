from  rest_framework.viewsets import ModelViewSet
from  pontosTuristicos.models import PontoTuristico
from .serializers import PontosTuristicosSerializer

class PontoTuristicoV (ModelViewSet):

    queryset = PontoTuristico.objects.all()
    serializer_class = PontosTuristicosSerializer  # import do arq serializers

