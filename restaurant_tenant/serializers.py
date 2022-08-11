from rest_framework import serializers

from restaurant_tenant.models import Item, Category, Menu


class ItemSerializer(serializers.ModelSerializer):
    model = Item
    fields = ("id", "name", "description", "price", "category")


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "items")


class MenuSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = Menu
        fields = ("id", "content", "restaurant", "categories")
