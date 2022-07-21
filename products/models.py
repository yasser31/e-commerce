from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from .mixins import ProductMixin, CategoryMixin


class Category(CategoryMixin):
    pass


class Product(ProductMixin):
    pass


class Attribute(models.Model):
    name = models.CharField(max_length=256, unique=True)
    product_variants = models.ManyToManyField(
        'ProductVariant', related_name="attributes")
    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    name = models.CharField(max_length=256, default="")
    sku = models.CharField(max_length=256, default="")
    product = models.ForeignKey(Product, related_name="variants",
                                on_delete=models.CASCADE)
    
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    value = models.CharField(max_length=256)
    attribute = models.ForeignKey(Attribute, related_name="values",
                                  on_delete=models.CASCADE)
    product_variant = models.ManyToManyField(ProductVariant, related_name="attr_values",
                                             blank=True)

    def __str__(self):
        return self.value


class Image(models.Model):

    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    product = models.ForeignKey(ProductVariant, related_name="images",
                                on_delete=models.CASCADE, null=True, blank=True)

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
