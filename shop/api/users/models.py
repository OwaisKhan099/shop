from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    Phone = models.CharField(max_length=20, blank=False)


    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
