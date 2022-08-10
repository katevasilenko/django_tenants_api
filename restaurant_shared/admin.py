from django.contrib import admin

from restaurant_shared.models import RestaurantPublic, Menu


@admin.register(RestaurantPublic)
class RestaurantTPublicAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('content',)
