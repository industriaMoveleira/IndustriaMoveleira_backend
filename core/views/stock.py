from rest_framework.viewsets import ModelViewSet
from core.models import Stock
from core.serializers import StockSerializer

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer