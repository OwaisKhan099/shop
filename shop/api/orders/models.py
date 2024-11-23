from django.db import models
from ..users.models import CustomUser
from django.db import models
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    product_names = models.CharField(max_length=50)
    total_products = models.CharField(max_length=50, default=0)
    transaction_id= models.CharField(max_length=50, default=0)
    amount = models.CharField(max_length=50, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


