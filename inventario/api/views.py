from rest_framework import viewsets, permissions
from inventario.models import Producto
from inventario.api.serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer