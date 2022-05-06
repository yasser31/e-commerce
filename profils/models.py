from django.db import models
from users.models import User


class Profil(models.Model):

    photo = models.ImageField(blank=True, upload_to='uploads/', null=True)
    description = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
