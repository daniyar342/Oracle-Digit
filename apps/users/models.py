from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from common.base_model import BaseModel
from .usermanager import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.username