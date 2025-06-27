from rest_framework.serializers import ModelSerializer
from core.models import OrderedItem

class OrderedItemSerializer(ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = '__all__'
        depth = 1