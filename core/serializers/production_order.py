from rest_framework.serializers import ModelSerializer
from core.models import ProductionOrder

class ProductionOrderSerializer(ModelSerializer):
    class Meta:
        model = ProductionOrder
        fields = '__all__'
        depth = 1