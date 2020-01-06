from  rest_framework.viewsets import ModelViewSet
from  localizacao.models import Localizacao
from .serializers import LocalizacaoSerializer

class LocalizacaoViewSets (ModelViewSet):

    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer 