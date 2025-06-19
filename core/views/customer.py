from rest_framework.viewsets import ModelViewSet
from core.models import Customer
from core.serializers import CustomerSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer