from django.db import models
from users.models import User

class Publication(models.Model):
    
    added_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField(blank=True, default="text")
