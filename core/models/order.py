from django.db import models
from .customer import Customer

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="orders")
    date_order = models.DateField()
    quantity_items = models.IntegerField()
    
    def __str__(self):
        return f"{self.customer} - {self.quantity_items} items"