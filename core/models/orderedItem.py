from django.db import models
from .product import Product
from .order import Order

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="orderedItem")
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="orderedItem")
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=4, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)

