from django.urls import path, include
from rest_framework import routers

from tenant.views import (
    RestaurantViewSet, CategoryViewSet, ProductViewSet, MenusViewSet
)

router = routers.DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
router.register("menus", MenusViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "public"
