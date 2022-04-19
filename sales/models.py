from django.db import models
from users.models import User
from products.models import Product

class TotalSale(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(blank=True, default=0)


class Sale(models.Model):

    total = models.IntegerField(blank=True, default=0)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)