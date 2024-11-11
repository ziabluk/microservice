from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from .models import Product, Storage
from .serializers import ProductSerializer, StorageSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ('code', 'group', 'storage')
    filter_backends = [DjangoFilterBackend]


class WarehouseProductListView(ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
