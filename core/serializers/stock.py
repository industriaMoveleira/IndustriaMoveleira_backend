from rest_framework.serializers import ModelSerializer
from core.models import Stock

class StockSerializer(ModelSerializer):
    model = Stock
    fields = '__all__'
    depth = 1