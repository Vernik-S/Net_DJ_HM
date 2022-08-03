from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', ]
    pagination_class = PageNumberPagination
    pagination.PageNumberPagination.page_size = 2

class StockCustomFilter(SearchFilter):
    search_param = "products_search"

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, StockCustomFilter]
    filterset_fields = ['id', 'products', ]
    search_fields = ['products__title', 'products__description']
    #SearchFilter.search_param = "products_search" #для допзадания. Параметр поиска был изменен чтобы не было конфликта с поиском по id продукта
    pagination_class = LimitOffsetPagination
