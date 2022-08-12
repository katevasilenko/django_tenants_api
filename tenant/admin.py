from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from tenant.models import Restaurant, Category, Product, Menus


@admin.register(Restaurant)
class RestaurantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Menus)
