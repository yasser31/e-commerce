from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    address = models.CharField(default="", blank=True, max_length=256)
    confirmed = models.BooleanField(null=True, default=False)
    
    def __str__(self):
        return self.username

