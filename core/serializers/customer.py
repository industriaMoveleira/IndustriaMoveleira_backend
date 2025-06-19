from rest_framework import ModelSerializer
from core.models import Customer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1