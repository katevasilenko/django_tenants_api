from django.contrib import admin

from restaurant_tenant.models import Restaurant, Menu


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('content', 'categories')
