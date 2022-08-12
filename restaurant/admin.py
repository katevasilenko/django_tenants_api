from django.contrib import admin

from restaurant.models import Menu, Item, Category

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Menu)
