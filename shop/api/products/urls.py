from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'', views.ProductView)

urlpatterns = [
    path("", include(router.urls))
]