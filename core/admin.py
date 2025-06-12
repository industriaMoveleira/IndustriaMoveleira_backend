from django.contrib import admin
from core.models import Customer, Order, Funcionario


admin.site.register(Funcionario)
admin.site.register(Customer)
admin.site.register(Order)

