from rest_framework import serializers
from apps.products.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Product
        fields = ['id',"name","description","price","category","images"]
        

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name","owner"]
        
    