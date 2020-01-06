from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSets (ModelViewSet):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer