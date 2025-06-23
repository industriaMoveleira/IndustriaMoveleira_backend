from rest_framework.viewsets import ModelViewSet
from core.models import MateriaPrima
from core.serializers import MateriaPrimaSerializer

class MateriaPrimaViewSet(ModelViewSet):
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer