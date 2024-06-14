from django.shortcuts import render
from django.http import JsonResponse, request
from rest_framework import serializers, viewsets
from .serializers import ProductSerializer
from .models import Products
# Create your views here.

def index(request):
    return JsonResponse({"status":"This is the product"})
class ProductView(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductSerializer

