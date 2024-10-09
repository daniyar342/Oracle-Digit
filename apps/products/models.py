from django.db import models
from common.base_model import BaseModel
from ..users.models import CustomUser

class Category(BaseModel):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    
class Image(models.Model):
    image = models.ImageField(upload_to='product_images/')
    
    
class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)