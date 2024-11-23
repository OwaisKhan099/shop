from .serializers import OrderSerializer
from .models import Order
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from django.http import JsonResponse
# Create your views here.

def ValidataUserSession(id,token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request, id, token):
    if not ValidataUserSession(id, token):
        return JsonResponse({'Error':'Please, login', 'Code':'1'})
    if request.method == "POST":
        user_id = id
        transanction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products_name = request.POST['total_products']
        total_products = len(products_name.split(',')[:-1])
        UserModel = get_user_model()

        try :
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({"Error":"User does not exist"})
        ordr = Order(user=user,product_names=products_name,total_products=total_products,transaction_id=transanction_id,amount=amount)
        ordr.save()
        return JsonResponse({'success':True,'Error':False, 'msg':'order_list'})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer