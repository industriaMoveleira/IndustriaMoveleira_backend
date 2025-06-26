from rest_framework.serializers import ModelSerializer
from core.models import Stock

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        depth = 1