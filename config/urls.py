from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CustomerViewSet, ProductViewSet, FuncionarioViewSet, MateriaPrimaViewSet, StockViewSet, OrderViewSet, OrderedItemViewSet, ProductionOrderViewSet
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'employees', FuncionarioViewSet)
router.register(r'rawMaterials', MateriaPrimaViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderedItems', OrderedItemViewSet)
router.register(r'productionorders', ProductionOrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
