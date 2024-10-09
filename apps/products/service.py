from common.base_service import ServicesManager
from django.db import transaction
from .models import Product,Category


class ProductService(ServicesManager):
    model = Product
    
    @classmethod
    def create(cls, **data):
        with transaction.atomic():
            product = cls.model.objects.create(
                name=data.get('name'),
                price=data.get('price',0),
                description=data.get('description'),
                owner=data.get('owner'),
                category=data.get('category'),
                image=data.get('image'),
            )
        return product
    
    @classmethod
    def update(cls, obj, **data):
        with transaction.atomic():
            obj.name = data.get('name', obj.name)
            obj.price = data.get('price', obj.price)
            obj.description = data.get('description', obj.description)
            obj.owner = data.get('owner', obj.owner)
            obj.category = obj.category
            obj.images = data.get('images', obj.images)
            obj.save()
        return obj
    
    
class CategoryService(ServicesManager):
    model = Category
    
    @classmethod
    def create(cls, **data):
        with transaction.atomic():
            category = cls.model.objects.create(
                name=data.get('name'),
                owner=data.get('owner'),
            )
        return category
    
    @classmethod
    def update(cls, obj, **data):
        with transaction.atomic():
            obj.name = data.get('name', obj.name)
            obj.owner = data.get('owner', obj.owner)
            obj.save()
        return obj
