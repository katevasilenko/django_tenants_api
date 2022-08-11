from rest_framework import serializers

from restaurant_shared.models import Restaurant, Category, Product, Menus


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "type", "description")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "category")


class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ("content", "restaurant", "categories")
