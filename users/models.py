from django.db import models

class User(models.Model):
    
    username = models.CharField(max_length=100, 
         default="username")
    password = models.CharField(max_length=100, default="password")
    email = models.EmailField(max_length=100, default="email")
    phone = models.IntegerField(default="0", blank=True)

    
    def __str__(self):
        return self.username


class Profil(models.Model):
    
    photo = models.ImageField(blank=True, upload_to='uploads/', max_length=100)
    description = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username