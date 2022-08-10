from django.db import models


class RestaurantPublic(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()


class Menu(models.Model):
    content = models.TextField()
    categories = models.ManyToManyField('Category')
    restaurant = models.ForeignKey(
        RestaurantPublic,
        on_delete=models.CASCADE,
        blank=True,
        default=''
    )


class Category(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    name = models.CharField(max_length=255)
