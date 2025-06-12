from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=120)
    telephone = models.CharField(max_length=15)
    date_birth = models.DateField()
    adress = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name