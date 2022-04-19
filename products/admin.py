from django.contrib import admin
from .models import Product, Image, Category


class ImageInLine(admin.StackedInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Category)