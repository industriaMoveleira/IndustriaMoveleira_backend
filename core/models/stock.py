from django.db import models 
from .product import Product
from .rawMaterial import MateriaPrima

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="stock")
    raw_material = models.ForeignKey(MateriaPrima, on_delete=models.PROTECT, related_name="stock")
    quantity = models.IntegerField()
    location = models.CharField(max_length=120)