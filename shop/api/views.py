from django.shortcuts import render
from django.http import request, HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return JsonResponse({'status': 'This is the api page'})