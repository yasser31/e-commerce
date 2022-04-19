from django.db import models
from products.models import Product


class Store(models.Model):
    products = models.ManyToManyField(Product)