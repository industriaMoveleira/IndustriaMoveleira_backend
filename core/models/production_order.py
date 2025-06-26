from django.db import models
from core.models import Product, Funcionario

class ProductionOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="production")
    quantity = models.IntegerField()
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=80)
    employee = models.ManyToManyField(Funcionario, related_name="production")