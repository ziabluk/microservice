from django.urls import path

from .views import ProductListView, WarehouseProductListView

urlpatterns = [
    path('products', ProductListView.as_view()),
    path('storages', WarehouseProductListView.as_view()),
]
