from django.shortcuts import render
from django.http import request, HttpResponse, JsonResponse
from .models import Category
from rest_framework import viewsets
from .serializers import CategorySerializer
# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()  #.order_by('name')
    serializer_class = CategorySerializer




def index(request):
    return JsonResponse({'status': 'This is the category page'})