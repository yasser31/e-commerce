from django.db import models
from publication.models import Publication
from io import BytesIO
from PIL import Image
from django.core.files import File


class Category(models.Model):
    category = models.CharField(max_length=255, default="")
    slug = models.SlugField(max_length=255, default="")
    
    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):

    name = models.CharField(max_length=255, default='name')
    sulg = models.SlugField()
    details = models.TextField(blank=True, null=True, default="text")
    category = models.ForeignKey(Category, related_name="products", on_delete=models.DO_NOTHING)
    publication = models.ForeignKey(Publication,related_name="products", 
                                      on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        ordering = ('-publication__added_date',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    
'''
class Color(models.Model):

    color = models.CharField(blank=True, max_length=255, default="white")
    product = models.ManyToManyField(Products)

class Price(models.Model):

    price = models.IntegerField(blank=True)
    product = models.ManyToManyField(Products)

class Surfaces(models.Model):

    surface = models.IntegerField(blank=True)
    product = models.ManyToManyField(Products)
'''

class Image(models.Model):

    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    product = models.ForeignKey(Product, related_name="images", 
                                  on_delete=models.DO_NOTHING, null=True, blank=True)

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return "http://127.0.0.1:8000" + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return "http://127.0.0.1:8000" + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail