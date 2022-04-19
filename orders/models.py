from django.db import models
from users.models import User
from carts.models import Cart


class Checking(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.DO_NOTHING)
    
