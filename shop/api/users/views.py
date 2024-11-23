import os

from django.shortcuts import render
from django.http import request, HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from .serializers import  UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import random
import re
# Create your views here.
def generate_session_token(length=10):

    return "".join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(0,10)]) for _ in range(length))

@csrf_exempt
def signin(request):
    if request.method != "POST":
        return HttpResponse("Request method is not Post")

    # USERNAME = request.POST["email"]
    # PASSWORD = request.POST["password"]
    # print( request.POST.keys(), request.body)
    USERNAME = request.POST.get('email')
    #USERNAME = request.POST.
    PASSWORD = request.POST.get("password")
    #PASSWORD = request.POST["password"]
    print("hhhh ",PASSWORD, USERNAME)
    if len(str(PASSWORD)) < 3:
        return JsonResponse({"error":"The length of PW is less than 3"})

    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email = USERNAME)
        if user.check_password(PASSWORD):
            # usr_dict = UserModel.objects.filter(
    #         #     email=USERNAME)
            usr_dict = UserModel.objects.filter(email = USERNAME).values().first()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({"error": "previous session exists"})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request,user)
            return JsonResponse({'token':token , "user" : usr_dict})
        else:
            return JsonResponse({"error":"Entered wrong password"})

    except UserModel.DoesNotExist:
        return JsonResponse({"Error": "Invalid Email"})
@csrf_exempt
def signout(request, id):
    logout(request)
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({"error":"Invalid User id"})
    return  JsonResponse({"success":"logout success"})


class UserViewSet(viewsets.ModelViewSet):
    print("user view")
    permission_classes_by_action = {"create":[AllowAny]}
    queryset = CustomUser.objects.all().order_by("id")
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


def index(request):
    return HttpResponse("This is user application")

generate_session_token(10)