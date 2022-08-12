from django.urls import path, include
from rest_framework import routers

from restaurant.views import ItemViewSet, CategoryViewSet, MenuViewSet

router = routers.DefaultRouter()
router.register("items", ItemViewSet)
router.register("categories", CategoryViewSet)
router.register("menu", MenuViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "tenant"
