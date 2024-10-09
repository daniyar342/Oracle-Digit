from django.shortcuts import render

from api.viewsets import CustomModelViewSet
from .service import ProductService, CategoryService
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(CustomModelViewSet):
    validate_serializer_class = ProductSerializer
    serializer_class = ProductSerializer
    service_class = ProductService
    select_ = ['category', 'images']


class CategoryViewSet(CustomModelViewSet):
    validate_serializer_class = CategorySerializer
    serializer_class = CategorySerializer
    service_class =CategoryService
    select_ = ['owner']