from common.base_service import ServicesManager
from .models import CustomUser
from django.db import transaction
from .usermanager import CustomUserManager

class CustomUserService(ServicesManager):
    model = CustomUser
    
    @classmethod
    def create(cls, **validated_data):
        with transaction.atomic():
            username = validated_data.get('username')
            password = validated_data.get('password')
            email = validated_data.get('email')
            
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            
        return user