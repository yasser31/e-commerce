from django.db import models
from users.models import User
from orders.models import Checking

class Payment(models.Model):

    details = models.TextField(blank=True, default="text")
    total = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checking = models.OneToOneField(Checking, on_delete=models.DO_NOTHING, default=1)
