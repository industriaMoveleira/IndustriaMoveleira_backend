from rest_framework.viewsets import ModelViewSet
from core.models import OrderedItem
from core.serializers import OrderedItemSerializer

class OrderedItemViewSet(ModelViewSet):
    queryset = OrderedItem.objects.all()
    serializer_class = OrderedItemSerializer