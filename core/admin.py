from django.contrib import admin
from core.models import Customer, Order, Funcionario, MateriaPrima, Product, ProductionOrder, Stock, OrderedItem

admin.site.register(Funcionario)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(MateriaPrima)
admin.site.register(Product)
admin.site.register(ProductionOrder)
admin.site.register(Stock)
admin.site.register(OrderedItem)