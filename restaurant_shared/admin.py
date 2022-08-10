from django.contrib import admin

from restaurant_shared.models import Restaurant, Menus, Category, Product

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Menus)
