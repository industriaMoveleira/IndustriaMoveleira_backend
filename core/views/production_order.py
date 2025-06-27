from rest_framework.viewsets import ModelViewSet
from core.models import ProductionOrder
from core.serializers import ProductionOrderSerializer

class ProductionOrderViewSet(ModelViewSet):
    queryset = ProductionOrder.objects.all()
    serializer_class = ProductionOrderSerializer