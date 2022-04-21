from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    address = models.CharField(default="", blank=True, max_length=256)

    def __str__(self):
        return self.username


class Profil(models.Model):
    
    photo = models.ImageField(blank=True, upload_to='uploads/', max_length=100)
    description = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username