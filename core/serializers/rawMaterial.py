from rest_framework.serializers import ModelSerializer
from core.models import MateriaPrima

class MateriaPrimaSerializer(ModelSerializer):
    class Meta:
        model = MateriaPrima
        fields = '__all__'
        depth = 1