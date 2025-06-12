from django.contrib import admin
from core.models import Customer, Order, Funcionario, MateriaPrima, Product, ProductionOrder

admin.site.register(Funcionario)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(MateriaPrima)
admin.site.register(Product)
admin.site.register(ProductionOrder)
