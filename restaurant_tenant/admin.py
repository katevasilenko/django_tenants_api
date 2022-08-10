from django.contrib import admin

from restaurant_tenant.models import Menu, Item, Category

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Menu)
