from django.db import models

from restaurant_shared.models import RestaurantPublic


class Restaurant(models.Model):
    restaurant_public = models.OneToOneField(
        RestaurantPublic,
        blank=True,
        default='',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()


class Menu(models.Model):
    content = models.TextField()
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=63)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
