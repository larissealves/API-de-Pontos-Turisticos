from rest_framework.serializers import ModelSerializer
from pontosTuristicos.models import PontoTuristico

class PontosTuristicosSerializer (ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'decricao', 'localizacao', 'aprovado', 'foto')


