from django.shortcuts import render
from django.http import request, JsonResponse, HttpResponse
# Create your views here.
def index(request):
    return JsonResponse({'Page':'This is users" page'})