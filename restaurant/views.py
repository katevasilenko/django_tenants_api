from rest_framework import viewsets, mixins

from restaurant.models import Item, Category, Menu
from restaurant.serializers import (
    ItemSerializer, CategorySerializer, MenuSerializer
)


class ItemViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
