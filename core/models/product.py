from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    typeProduct = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - R${self.price}"
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"